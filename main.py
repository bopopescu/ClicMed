import settings
import log
# ---------------------------------------------------------------------------------------------------------------------
# Main execution of program

log.init_log("user_mgmt")
settings.login.login_window(settings.root)
settings.root.mainloop()
