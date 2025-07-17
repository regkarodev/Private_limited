"""
Centralized logging system for NSWS automation project.
Provides structured logging with different levels and proper formatting.
"""

import logging
import os
from datetime import datetime


class AutomationLogger:
    """Centralized logger for automation tasks"""
    
    def __init__(self, name="NSWS_Automation", log_level=logging.INFO):
        self.logger = logging.getLogger(name)
        self.logger.setLevel(log_level)
        
        # Remove existing handlers to avoid duplicates
        if self.logger.handlers:
            self.logger.handlers.clear()
        
        # Create logs directory if it doesn't exist
        if not os.path.exists('logs'):
            os.makedirs('logs')
        
        # Create formatters
        detailed_formatter = logging.Formatter(
            '%(asctime)s - %(name)s - %(levelname)s - %(funcName)s:%(lineno)d - %(message)s'
        )
        
        simple_formatter = logging.Formatter(
            '%(asctime)s - %(levelname)s - %(message)s'
        )
        
        # File handler for detailed logs
        file_handler = logging.FileHandler(
            f'logs/automation_{datetime.now().strftime("%Y%m%d")}.log',
            encoding='utf-8'
        )
        file_handler.setLevel(logging.DEBUG)
        file_handler.setFormatter(detailed_formatter)
        
        # Console handler for important messages
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        console_handler.setFormatter(simple_formatter)
        
        # Add handlers to logger
        self.logger.addHandler(file_handler)
        self.logger.addHandler(console_handler)
    
    def debug(self, message):
        """Log debug information"""
        self.logger.debug(message)
    
    def info(self, message):
        """Log general information"""
        self.logger.info(message)
    
    def warning(self, message):
        """Log warning messages"""
        self.logger.warning(message)
    
    def error(self, message):
        """Log error messages"""
        self.logger.error(message)
    
    def critical(self, message):
        """Log critical error messages"""
        self.logger.critical(message)
    
    def log_action(self, action, selector_type, selector_value, success=True):
        """Log automation actions with structured format"""
        status = "SUCCESS" if success else "FAILED"
        message = f"[{action}] {selector_type}='{selector_value}' - {status}"
        
        if success:
            self.info(message)
        else:
            self.error(message)
    
    def log_step(self, step_name, details=""):
        """Log major automation steps"""
        message = f"STEP: {step_name}"
        if details:
            message += f" - {details}"
        self.info(message)


# Global logger instance
automation_logger = AutomationLogger()

# Convenience functions for easy access
def log_debug(message):
    automation_logger.debug(message)

def log_info(message):
    automation_logger.info(message)

def log_warning(message):
    automation_logger.warning(message)

def log_error(message):
    automation_logger.error(message)

def log_critical(message):
    automation_logger.critical(message)

def log_action(action, selector_type, selector_value, success=True):
    automation_logger.log_action(action, selector_type, selector_value, success)

def log_step(step_name, details=""):
    automation_logger.log_step(step_name, details) 