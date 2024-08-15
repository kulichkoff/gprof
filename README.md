# GPROF

This is a very simple script that will help you to switch between your git profiles.
It is very useful if your job and home profiles are different.

## Prerequisites

- **Python 3.11** or earlier
- Unix-like system (not tested on windows yet)

## How to use

1. Create the config file in your home directory `~/.config/gprof/profiles`
2. Configure some profiles:
   
```toml
[home]
name = "My pretty name"
email = "personal@example.com"

[job]
name = "My pretty name"
email = "job_email@google.com"
```

3. Here you are! Just start the script:

```shell
$ python3 gprof.py home|job|any_another_profile
# python3 gprof.py job
```
