from dynaconf import Dynaconf

settings = Dynaconf(
  settings_files=['settings.toml'],
  environments=True,
  env_switcher='ENV_FOR_DYNACONF'
)

print(f"App Name: {settings.app_name}")
print(f"Debug: {settings.debug}")
print(f"Database URL: {settings.database_url}")
