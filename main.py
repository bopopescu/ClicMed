import settings
# ---------------------------------------------------------------------------------------------------------------------
# Main execution of program

settings.log.init_log("user_mgmt")
settings.login.login_window(settings.root)
settings.root.mainloop()
