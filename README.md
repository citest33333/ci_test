# CI test

## Editing GitHub Workflows

Do not edit `.github/workflows/*.yml` directly. To support yaml anchors/aliasing, we can edit `.github/*.yml` and feed it as source to `.github/gwp.py`.

- Install [yq](https://mikefarah.gitbook.io/yq/#install) if not already installed
- Edit the desired `.github/*.yml`
- cd into `.github` and run `python gwp.py`. This will glob for all `*.yml`, expand out the aliases, and dump it to `.github/workflows`
