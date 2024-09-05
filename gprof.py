import os
from dataclasses import dataclass
from argparse import ArgumentParser
import tomllib # ! requires python 3.11


@dataclass
class GitProfile:
  email: str
  name: str


def change_profile(profile: GitProfile):
  os.system(f"git config --global --replace-all user.name \"{profile.name}\"")
  os.system(f"git config --global --replace-all user.email \"{profile.email}\"")


def get_profile_config(profile_name: str) -> GitProfile:
  profiles_config_path = os.path.expanduser("~/.config/gprof/profiles")
  with open(profiles_config_path, "rb") as file:
    profiles_config = tomllib.load(file)
    certain_profile_config = profiles_config.get(profile_name)
    if certain_profile_config is None:
      raise Exception(f"Cannot find profile with name \"{profile_name}\"")
    return GitProfile(
      certain_profile_config.get("email"), 
      certain_profile_config.get("name")
    )
     


def main():
  parser = ArgumentParser(description="Change your Git profile easily")
  parser.add_argument("profile_name", type=str, help="Git profile name in config")
  args = vars(parser.parse_args())
  
  profile_name = args.get('profile_name')

  try:
    profile = get_profile_config(profile_name)
    change_profile(profile)
  except Exception as err:
    print("Could not change git profile:", err)
    return

  print(f"\t> Changed your git profile to {profile.email}")
  


if __name__ == "__main__":
    main()
