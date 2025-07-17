# NSWS Automation

A robust Python automation framework for interacting with the NSWS (National Single Window System) web portal. It features reliable element handling, advanced input simulation using Chrome DevTools Protocol (CDP), and a centralized logging system for debugging and monitoring.

## Features
- **Reliable Web Automation:**
  - Retry logic for finding elements
  - Robust input simulation using CDP
  - Bulk execution of UI actions
- **Centralized Logging:**
  - Structured logs to file and console
  - Log levels: DEBUG, INFO, WARNING, ERROR, CRITICAL
  - Action and step logging for traceability
- **Configurable:**
  - All selectors, URLs, and credentials are managed in `config.py`
- **Extensible:**
  - Modular design for easy extension and maintenance

## Project Structure
```
├── function.py      # Main automation logic and helpers
├── logger.py        # Centralized logging system
├── config.py        # Configuration for selectors, URLs, credentials
├── requirements.txt # Python dependencies
├── README.md        # Project documentation
```

## Setup
1. **Clone the repository:**
   ```bash
   git clone <your-repo-url>
   cd private_limited
   ```
2. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```
3. **Configure settings:**
   - Edit `config.py` to update URLs, credentials, and selectors as needed.

## Usage
- **Set up the Selenium WebDriver** in your main script and pass it to the automation functions:
  ```python
  from selenium import webdriver
  from function import set_driver, find_element_with_retry, send_text_with_cdp

  driver = webdriver.Chrome()
  set_driver(driver)
  # Now use the automation functions
  ```
- **Bulk execute actions:**
  ```python
  from function import bulk_execute
  actions = [
      {"action": "click_element", "css_selector": "#my-button"},
      {"action": "send_text", "id": "username", "keys": "myuser"}
  ]
  results = bulk_execute(actions)
  ```

## Logging
- All logs are written to the `logs/` directory and printed to the console.
- Use the convenience functions from `logger.py`:
  - `log_debug(message)`
  - `log_info(message)`
  - `log_warning(message)`
  - `log_error(message)`
  - `log_critical(message)`
  - `log_action(action, selector_type, selector_value, success=True)`
  - `log_step(step_name, details="")`

## Configuration
- All selectors, URLs, credentials, and timeouts are managed in `config.py`.
- Update this file to match your environment and automation needs.

## Requirements
- Python 3.8+
- Selenium

## Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.

## License
[MIT](LICENSE)
