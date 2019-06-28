import settings
# ---------------------------------------------------------------------------------------------------------------------
# Main execution of program

settings.log.init_log()
settings.login.login_window(settings.root)
settings.root.mainloop()
