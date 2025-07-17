# NSWS_Automation/enhanced_functions.py

"""
Enhanced web automation functions with robust reliability checks, including
the Chrome DevTools Protocol (CDP) for ultimate input simulation.
"""

import time
import json
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
from logger import log_debug, log_info, log_warning, log_error
from config import DROPDOWN_CSS
from selenium.webdriver.remote.webdriver import WebDriver
from typing import Any

# Global driver variable
driver: WebDriver | None = None

def set_driver(webdriver_instance):
    """Set the global driver instance. Called from login.py."""
    global driver
    driver = webdriver_instance
    log_info("Driver instance set for enhanced functions")

def find_element_with_retry(selector_type, selector_value, retries=3, timeout=10):
    """Finds an element with a retry mechanism."""
    if driver is None:
        log_error("Driver is not set.")
        return None
    for i in range(retries):
        try:
            by_mapping = {
                'xpath': By.XPATH, 'id': By.ID, 'css_selector': By.CSS_SELECTOR,
                'class_name': By.CLASS_NAME, 'name': By.NAME
            }
            element = WebDriverWait(driver, timeout).until(
                EC.presence_of_element_located((by_mapping[selector_type], selector_value))
            )
            return element
        except TimeoutException:
            log_warning(f"Element '{selector_value}' not found on attempt {i+1}.")
    log_error(f"Element '{selector_value}' not found after {retries} attempts.")
    return None

def send_text_with_cdp(element, text: str):
    """
    Types text into a focused element using CDP Input.dispatchKeyEvent.
    This is the most reliable method for modern web apps.
    """
    log_debug(f"Typing '{text}' using CDP.")
    
    # CDP commands are sent to the currently focused element, so we must click it first.
    element.click()
    time.sleep(0.1) # Brief pause to ensure focus

    if driver is None:
        log_error("Driver is not set.")
        return False

    for char in text:
        key_code = ord(char)
        
        # Dispatch keyDown, char, and keyUp events to simulate a real key press
        driver.execute_cdp_cmd('Input.dispatchKeyEvent', {
            'type': 'keyDown', 'windowsVirtualKeyCode': key_code, 'key': char
        })
        driver.execute_cdp_cmd('Input.dispatchKeyEvent', {
            'type': 'char', 'text': char
        })
        driver.execute_cdp_cmd('Input.dispatchKeyEvent', {
            'type': 'keyUp', 'windowsVirtualKeyCode': key_code, 'key': char
        })
    return True

def extract_selector_info(action):
    """Extracts selector information from an action dictionary."""
    for key in ['id', 'xpath', 'css_selector', 'class_name', 'name']:
        if key in action:
            return {"selector_type": key, "selector_value": action[key]}
    return None

def _execute_single_action(action):
    """Internal helper to execute a single action using the most robust method."""
    selector_info = extract_selector_info(action)
    if not selector_info:
        return {"success": False, "error": "Invalid selector in action"}

    action_type = action.get("action")
    selector_type = selector_info["selector_type"]
    selector_value = selector_info["selector_value"]
    
    log_info(f"Executing action: {action_type} on '{selector_value}'")

    element = find_element_with_retry(selector_type, selector_value)
    if not element:
        return {"success": False, "error": "Element not found"}

    try:
        if action_type == "send_text":
            keys = action.get("keys", "")
            success = send_text_with_cdp(element, keys)
            # Verification
            if element.get_attribute('value') == keys:
                log_debug(f"CDP input verified for '{selector_value}'.")
                return {"success": True}
            else:
                log_error(f"CDP input failed verification for '{selector_value}'.")
                return {"success": False, "error": "CDP input verification failed"}

        elif action_type == "click_element":
            element.click()
            return {"success": True}

        elif action_type == "upload_file":
            file_path = action.get("keys", "")
            element.send_keys(file_path)
            log_debug(f"File path '{file_path}' sent to '{selector_value}'.")
            return {"success": True}
            
    except Exception as e:
        log_error(f"Failed to execute action on '{selector_value}': {e}")
        return {"success": False, "error": str(e)}

    return {"success": False, "error": "Unknown action type"}

def handle_subform1_dropdown(data=None):
    """
    Handle the subForm1Dropdown selection based on JSON data.
    
    Args:
        data: Optional data dictionary. If None, will load from textdb.json
    
    Returns:
        dict: Results of the dropdown selection process
    """
    log_info("Starting subForm1Dropdown handling")
    
    try:
        # Load data if not provided
        if data is None:
            with open('textdb.json', 'r') as json_file:
                data = json.load(json_file)
        
        # Get dropdown options from JSON
        dropdown_options = data["documentUpload"]["subForm1Dropdown"]
        log_info(f"Dropdown options: {dropdown_options}")
        
        # First click to open the dropdown
        open_dropdown_action = [{"action": "click_element", "css_selector": DROPDOWN_CSS}]
        result = bulk_execute(open_dropdown_action)
        
        if not result["executed"]:
            log_error("Failed to open dropdown")
            return {"success": False, "error": "Failed to open dropdown"}
        
        time.sleep(1)  # Wait for dropdown to open
        
        # Prepare actions for selecting options
        selection_actions = []
        
        # Handle first 4 options (1-4) with standard selectors
        option_names = list(dropdown_options.keys())
        for i in range(1, 5):
            if i <= len(option_names):
                option_name = option_names[i-1]
                if dropdown_options[option_name]:
                    css_selector = f"body > div:nth-child(19) > div > div > div > div > div > div.ant-select-tree-list > div > div > div > div:nth-child({i})"
                    selection_actions.append({
                        "action": "click_element", 
                        "css_selector": css_selector
                    })
                    log_info(f"Will select option {i}: {option_name}")
        
        # Handle the last option (accelerators) with different selector
        if "accelerators" in dropdown_options and dropdown_options["accelerators"]:
            css_selector = "body > div:nth-child(19) > div > div > div > div > div > div.ant-select-tree-list > div > div > div > div.ant-select-tree-treenode.ant-select-tree-treenode-switcher-close.ant-select-tree-treenode-leaf-last"
            selection_actions.append({
                "action": "click_element", 
                "css_selector": css_selector
            })
            log_info("Will select accelerators option")
        
        # Execute all selection actions
        if selection_actions:
            results = bulk_execute(selection_actions)
            log_info(f"Dropdown selection completed: {results['summary']}")
            return {"success": True, "results": results}
        else:
            log_info("No dropdown options selected based on JSON configuration")
            return {"success": True, "message": "No options to select"}
            
    except FileNotFoundError:
        log_error("textdb.json not found")
        return {"success": False, "error": "textdb.json file not found"}
    except json.JSONDecodeError as e:
        log_error(f"Error parsing textdb.json: {e}")
        return {"success": False, "error": "Invalid JSON format"}
    except Exception as e:
        log_error(f"Error in handle_subform1_dropdown: {str(e)}")
        return {"success": False, "error": str(e)}

def bulk_execute(actions):
    """
    Executes a list of actions sequentially, using the robust CDP method for inputs.
    """
    log_info(f"Starting execution of {len(actions)} actions.")
    results: dict[str, Any] = {"executed": [], "failed": []}

    for i, action in enumerate(actions):
        action_result = _execute_single_action(action)
        
        if action_result["success"]:
            results["executed"].append({"index": i, "action": action})
        else:
            results["failed"].append({"index": i, "action": action, "error": action_result["error"]})
        
        # Add small delay between actions for dropdown selections
        if action.get("action") == "click_element" and len(actions) > 1:
            time.sleep(0.5)

    total = len(actions)
    successful = len(results["executed"])
    failures = len(results["failed"])
    summary = f"Execution summary: {successful}/{total} actions succeeded, {failures} failed."
    results["summary"] = summary
    log_info(summary)

    return results