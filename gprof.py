import sys
import os
from dataclasses import dataclass
import tomllib # ! requires python 3.11


@dataclass
class GitProfile:
  email: str
  name: str


def change_profile(profile: GitProfile):
  pass


def get_profile_config(profile_name: str):
   pass


def main():
  # parse args
  args = sys.argv[1:]
  if len(args) != 1:
    print("Usage:\n\tgprof [profile_name]")
    return
  
  profile_name = args[0]

  # load specific profile
  profiles_config_path = os.path.expanduser("~/.config/gprof/profiles")
  with open(profiles_config_path, "rb") as file:
    profiles_config = tomllib.load(file)
    certain_profile_config = profiles_config.get(profile_name)
    if certain_profile_config is None:
      print(f"Cannot find the profile with the name \"{profile_name}\"")
      return
    profile = GitProfile(
      certain_profile_config.get("email"), 
      certain_profile_config.get("name")
    )

  os.system(f"git config --global --replace-all user.name \"{profile.name}\"")
  os.system(f"git config --global --replace-all user.email \"{profile.email}\"")
  print(f"\t> Changed your git profile to {profile.email}")
  


if __name__ == "__main__":
    main()
