# GitHub Organization Metadata
This repository contains metadata for [TheBastionBot] GitHub Organization.


## FAQs

#### How to add custom avatars to your profile card, in the [contributors] page?
1.  Edit the `data/avatars.json` file in this repository and add the link to
    an valid image for your GitHub username.
    For example,
    ```json
    "k3rn31p4nic": "https://resources.bastionbot.org/assets/266290969974931457.png"
    ```

2.  Run the members' metadata generator
    ```bash
    python generators/generateMembers.py
    ```
    *If you're not able to do it for some reason, it's okay. The member who'll be
    merging your pull request, will do it for you.*

3.  Commit changes (preferably with a descriptive commit message, like the one below)
    ```git
    avatars: add custom avatar for k3rn31p4nic
    ```
    *Don't use k3rn31p4nic, use your username!*

4.  Make a Pull Request to the origin (this) repository.

5.  A member with `write` access to this repository will review and merge your
    pull request and then your profile card in the [contributors] page will show
    the custom avatar.


<!-- Links -->
[TheBastionBot]: https://git.io/bastion
[contributors]: https://bastionbot.org/contributors
