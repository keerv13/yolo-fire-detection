#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys
import webbrowser
import threading
import time

def main():
    """Run administrative tasks."""
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'project.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    
    #Auto-open browser when running runserver
    if len(sys.argv) >= 2 and sys.argv[1] == 'runserver':
        def open_browser():
            time.sleep(2)  # Wait for server to start
            webbrowser.open('http://127.0.0.1:8000/upload/')
        
        threading.Thread(target=open_browser, daemon=True).start()
    
    execute_from_command_line(sys.argv)

if __name__ == '__main__':
    main()