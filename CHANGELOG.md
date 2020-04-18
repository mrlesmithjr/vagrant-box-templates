commit 7a9fbf64d4005aedc2addf94f3a6ffff6b32d199
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 17 23:26:36 2020 -0400

    Commented out gui = False for Windows
    
    For now I want this enabled for Windows rather than relying on RDP.

commit 675434f70aa2ce6dc60567d0b5bbf2304443b344
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Apr 5 21:20:24 2020 -0400

    Added Ubuntu 20.04 server

commit be01e38d75a7850706ecc36ee7be2a1379e795e4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Apr 5 21:20:00 2020 -0400

    Renamed Ubuntu Ermine to correct name

commit 4022b757d542c42adeb3d018b5063cd04574ea6e
Author: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Date:   Wed Feb 26 19:59:26 2020 +0000

    Bump ansible from 2.8.6 to 2.8.8
    
    Bumps [ansible](https://github.com/ansible/ansible) from 2.8.6 to 2.8.8.
    - [Release notes](https://github.com/ansible/ansible/releases)
    - [Commits](https://github.com/ansible/ansible/compare/v2.8.6...v2.8.8)
    
    Signed-off-by: dependabot[bot] <support@github.com>

commit caa8535c318b46672e0d861682b773a7be7b9e75
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Feb 13 14:28:39 2020 -0500

    Added symlinks for Debian/Ubuntu version numbers
    
    - To make things easier to find version numbers, symlinks were created
    to point to the respective version.

commit 419fd3d22eacb7b1106cdd150f716fc8930d5ed2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jan 29 08:43:00 2020 -0500

    Added dedicated Test desktop environment

commit 94bf44976cfbb009748c7afaa4b3146bb53a08a4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 20 15:32:57 2019 -0500

    Added Alpine 3.11
    
    - Latest version 3.11 has been released and Packer build has been
      updated

commit c40dff30c271e61fd2d9ca124651711e0e016c99
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 19 22:45:38 2019 -0500

    Added Linux Mint 19.3
    
    - Latest version was released and Packer build has been finished up

commit f397efb259ea56afd1c542ab2883c9ee00f89126
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 4 09:53:13 2019 -0500

    Added Elementary OS 5.1
    
    - This adds Elementary OS 5.1 support after finishing up Elementary OS
    5.1 Packer build. https://github.com/mrlesmithjr/packer-templates/pull/49

commit 58bcd40dee404c5417f66cd312f53be053d9cc53
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 4 01:12:31 2019 -0500

    Refactored LinuxMint
    
    - Refactored LinuxMint to reflect changes in Packer builds for
    LinuxMint. https://github.com/mrlesmithjr/packer-templates/pull/48

commit f3fcb7dfa9aae91b48ba42005e95f9fd67544df0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 3 18:35:37 2019 -0500

    Added Elementary OS 5.0
    
    - New Packer build added for Elementary OS 5.0 is working so we need to
    get it added here as well.

commit c4b1f719e9cf0c9fbaed4e6d73bd72827c1c02ee
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 25 23:00:07 2019 -0500

    Fixed Oracle Linux 7 synced folders
    
    - After doing some regression testing with updated Packer templates, it
    was discovered that VirtualBox guest additions for share folders is not
    functional. Changed synced folders to use rsync for now.

commit 163b991216a11fdf78d62995cb68e381b49015d7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 25 22:57:58 2019 -0500

    Added Oracle Linux 8
    
    - This adds Oracle Linux 8 after building with Packer

commit 16ad45d032379540aa6eb95716fb17f582633390
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 31 17:10:33 2019 -0400

    Changed graphics controller for Linux
    
    - This changes the graphics controller to vmsvga for Linux
    - This will be the going forward controller for Linux/3D
    - Closes #56

commit 4c1dc521c82c24d9eb9ad018ce7d30b6e7fe7168
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Oct 30 22:17:50 2019 -0400

    Fixed issue with repo info being displayed
    
    - This resolves the issue with displaying the repo info
    - Resolves #54

commit 712a3ceded4265fe5e09b9a6c613aaf74dad5b3e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Oct 30 22:10:24 2019 -0400

    Added Fedora 31
    
    - Added server/desktop
    - Closes #52

commit 92afc4c887fa25fde9bc51535b0a41d36bb118d8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Oct 27 21:12:04 2019 -0400

    Had to set default graphics to vboxvga
    
    - Just ran into an issue with the latest Virtualbox on Manjaro where it defaults to vmsvga

commit a1a64d28302d0c15de498cf5105f0605acd3cfc7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 25 15:53:45 2019 -0400

    Disabled Linux graphics controller
    
    - There is an issue with desktop versions displaying gui for now

commit 99f64f47bf7098a093167d542322b4b739948d99
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 25 01:23:28 2019 -0400

    Fixes issue when copying directories to new distro
    
    - Resolves #48

commit 66c342e5ced39a70af5ca6c97ee1649272531161
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 25 01:20:23 2019 -0400

    Change desktop and Windows graphics controller
    
    - Changed the default graphics driver for Linux to vmsvga
    - Changed the default graphics driver for Windows to vboxsvga
    - Closes #47

commit d9ac4cf24258d3109a0a8f2f220a511ee0bc1847
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 25 01:16:51 2019 -0400

    Added CentOS 8 desktop
    
    - This adds CentOS 8 desktop
    - Closes #46

commit fde68d9f522fa2583d2890f07bf7480588e34a7e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 24 21:13:57 2019 -0400

    Migrated prep script to utils.py
    
    - Migration of prep.sh has been completely migrated to utils.py
    - This brings more of the shell scripts into utils.py
    - The additional changes in this commit not related to utils.py or
    prep.sh are changes found by new functionality in utils.py

commit 742ef3b2a2f980c6b83f5bf3e3256b7b2806c8f3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 24 16:17:59 2019 -0400

    Added Ubuntu 19.10 Desktop
    
    - This adds Ubuntu 19.10 Desktop
    - Closes #43

commit 0c8ab4e1c0820308fb9e1ef7dd10d0bd90ed50e4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 24 12:55:11 2019 -0400

    Updated distro versions list

commit d2d4a4a64085cb2abec9bfbf7afc15776bf4946a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Oct 23 22:57:35 2019 -0400

    Updated utils.py and various tweaks
    
    - utils.py is now Python 3
    - Fixed issue with bootstrap script for CentOS 8
    - Updated Python requirements
    - Tweaked environment.yml.j2 Jinja2 template
    - Closes #41

commit d639fd9972202e520f25b1d7a4accaca416aecfe
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Oct 22 00:17:35 2019 -0400

    Added Ubuntu 19.10 Server
    
    - Closes #39

commit d22d7089ae890ec38e98a9c19f55be90f49a5e65
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Oct 5 14:46:28 2019 -0400

    Fixed issue with CentOS 8
    
    - CentOS 8 requires different Python package

commit 16c681e17282722ea72af5bf3135240f3d3847fc
Author: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Date:   Fri Oct 4 04:45:14 2019 +0000

    Bump pyyaml from 3.13 to 5.1
    
    Bumps [pyyaml](https://github.com/yaml/pyyaml) from 3.13 to 5.1.
    - [Release notes](https://github.com/yaml/pyyaml/releases)
    - [Changelog](https://github.com/yaml/pyyaml/blob/master/CHANGES)
    - [Commits](https://github.com/yaml/pyyaml/compare/3.13...5.1)
    
    Signed-off-by: dependabot[bot] <support@github.com>

commit ee5e7d3c7acc74e3a71303e00fce3bdfd52f82ca
Author: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com>
Date:   Fri Oct 4 04:45:13 2019 +0000

    Bump ansible from 2.7.2 to 2.7.12
    
    Bumps [ansible](https://github.com/ansible/community) from 2.7.2 to 2.7.12.
    - [Release notes](https://github.com/ansible/community/releases)
    - [Commits](https://github.com/ansible/community/commits)
    
    Signed-off-by: dependabot[bot] <support@github.com>

commit 1a938bd288b5306bad68b41aef6210b64b5a238e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 4 00:43:11 2019 -0400

    Added CentOS 8 Server
    
    - CentOS 8 Server is now working and available

commit 3074bd5cfe84648d678076730f6bb7531017a102
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 8 01:07:19 2019 -0400

    Added Debian 10 (Buster)

commit 3003c8e9b02b24ecc1150dc2e35c47341ef55e12
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 27 01:50:31 2019 -0400

    Added Alpine 3.10 release

commit 7c0f0d217e0c568576365ebf3beeec9d42675fb6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri May 17 08:18:26 2019 -0400

    Cleaned up tasks
    
    Some of the apk installs and pip installs needed to be cleaned up due to
    using loops.

commit 982f8c4023c92b243003a4ed993fc08cefe36deb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 15 22:40:26 2019 -0400

    Updated included distros

commit e266e4a66f31ac07142cf242ca5c36f6c889041b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 15 22:30:14 2019 -0400

    Added Arch latest
    
    Prior to this I was keeping up with each monthly version individually.
    This will be the going forward method. Because Arch uses a rolling
    release, this will be much easier to maintain.

commit 8ac291c42e431f720661756ac89acd543d2389f5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat May 11 22:48:17 2019 -0400

    Changed up Windows bootstrap processes

commit b4b443e17e373f8a524ce53f6c246416db1223bf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu May 9 09:10:28 2019 -0400

    Started cleaning up formatting based on rubocop linting

commit 911eb9e078a31120484dd5145d70827fc543b431
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu May 9 00:41:45 2019 -0400

    Added port forwarding for Windows RDP

commit 963a0b4a0f30ca1ac2e897b6c22d9de0ff60d4c0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 30 23:03:35 2019 -0400

    Added Fedora 28 desktop

commit 639f59cd53f3b99437b20384b6b7b3e1a69cc873
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 30 23:03:20 2019 -0400

    Added Fedora 30

commit c60341b9f2bf9fd956a1b47b9c6972d6195b7c62
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 23 19:16:30 2019 -0400

    Updated Python requirements based on Windows testing

commit 3f2440cd9a13df65c46c997c697573a43eae6cb4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 23 19:15:10 2019 -0400

    Forcing winrm SSL for Windows

commit 1526a08a4255a8c840553f9b1ecfc7b6478274c3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Apr 23 08:30:15 2019 -0400

    Added Windows 2008R2

commit 2b562f63c963473b9224c02ccdd136779d65505a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Apr 18 17:10:39 2019 -0400

    Added Ubuntu 19.04

commit 858786e8acfa2ee802984a568750b6776acfb02b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Apr 6 14:13:15 2019 -0400

    Fixed synced folders
    
    Using rsync as the virtualbox vboxsf service does not work correctly.

commit 6246ddbcd0617bbabffcf0466006239f52daaa3d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Apr 6 01:23:37 2019 -0400

    Added rsync args when using rsync to stop errors with symlinks

commit 4ee6d9e4980cfba0698e6ca7042fd0fca2345f36
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Apr 6 01:22:47 2019 -0400

    Changed synced folders to rsync due to issues with vboxsf

commit 7adad74404920398a54bb02bdd92b3bfef846f64
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 11 00:48:53 2019 -0400

    Added example of disabled synced folders

commit fafd2cf4d4e798ec6ce64aa8925e9cd35f9e3a48
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 11 00:46:52 2019 -0400

    Added ability to hard code function HGFS for VMware provider
    
    This resolves an issue that I am experiencing with CentOS and VMware
    provider. Have not been successful in getting a functional HGFS install
    for open-vm-tools for VMware provider.

commit 2cf3ae96fa02f279b7d458e97fbc76e8d91abd44
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 11 00:44:47 2019 -0400

    Added ability for VMware provider to use public ip for ssh
    
    This was added due to some issues I am currently experiencing with
    CentOS using VMware provider. Have not been able to resolve the issue as
    it does not seem to be an issue using VirtualBox provider.

commit a23350da2a0eb427b20735c393c22addcd7ea488
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Mar 11 00:41:47 2019 -0400

    Resolved issue with shared folders
    
    If disable_shared_folders is defined, but defined as false, the
    additional shared folders for scripts/playbooks was ignored.

commit 7e09ae91036efd665b8d674cc4e266d778ca9fd2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Mar 9 23:51:32 2019 -0500

    Disabled setting ethernet device for VMware

commit 15df675c32d29439a4886a8c5ffa6191d0ab9d85
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 8 22:12:46 2019 -0500

    Added ability to enable nested virtualization for VMware boxes

commit 214670c826de046e46e7e3c32ba63d8e1156f695
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 8 00:20:58 2019 -0500

    Added dev requirements

commit 91d429f8e5792b360063814d401f46313b562652
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Mar 8 00:20:48 2019 -0500

    Updated requirements

commit 90b969bc51658b858feb6500d38eec7fcbec0534
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Mar 5 22:24:05 2019 -0500

    Added Arch 2019.03.01

commit d58712466f3280fd3bafe4ae4a7b3624483cc532
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 27 00:38:24 2019 -0500

    Fixed issue with additional disks on VMware

commit 1e0ad27f51b9dfb59e08ae4a9390749b95c34980
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Feb 25 01:24:33 2019 -0500

    Updated FreeNAS environment for testing

commit 25fa2d1f102de93b906773b410dfea8bc6f8977b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Feb 24 02:19:26 2019 -0500

    Resolved issue when 2 disks are part of base box image

commit d6afeb10ab37af552cb6da2f79c4b40aeef65a1d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 23 01:01:17 2019 -0500

    Added support to manage synced_folders and hostname
    
    Can now enable in environments.yml whether to disable_synced_folders and
    manage_hostname.

commit 19c8b5ba7ae5cd19d1683d03c03f8fa5f88e6f8b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Feb 23 01:00:49 2019 -0500

    Added FreeNAS 11.2

commit 47349d2ef9a22d075473ba1956273d7fbcfc49d7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 8 13:30:18 2019 -0500

    Added Arch 2019-02-01

commit d9d6fce4f5dcaff07188983abe9fa6c61900af4d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jan 31 01:07:06 2019 -0500

    Added Alpine 3.9 release

commit 3ff10eda858b12b4000a7dc5bb2f43ef5e20dc52
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jan 10 18:33:37 2019 -0500

    Updated required Python modules

commit f0080a6a8a4e5e4004dda053daa71da5a41962e1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 8 17:35:54 2019 -0500

    Changed ansible_ssh variables to ansible_ vars w/out ssh

commit 43df22afe3a518387aa47cdea04c215f61fb53f9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 1 14:09:25 2019 -0500

    Added latest version of Arch

commit 76f8995a7fb82a4e865c6f500d818fc75466ff77
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 18 23:05:47 2018 -0500

    Added cleanup for host_vars when interfaces are not defined and ansible_ssh_host is defined from previous run

commit 42bd22b564ae485a8032df67ca91238e747cd13c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 18 22:34:36 2018 -0500

    Resolving issue with unit test validation of provision variable

commit 9fa2a9236c70e01729e9818460631fe3a9d8d620
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 18 12:04:01 2018 -0500

    Resolves #35

commit be69e45c2619c76feea0b892bc0031c168f335fe
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Dec 17 21:02:33 2018 -0500

    Added NethServer 7

commit 5300287a195f624fa2fb403841dfb6f66cd797fa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 14 01:06:37 2018 -0500

    Cleaned up playbook for package installs for depracations

commit ed168c0320cc3c82e5a2d7da39556a858c5d56b9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 14 01:02:53 2018 -0500

    Updated repo info

commit 4f5be3951199b111ae7aeffebac26e3754fd1358
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 14 00:58:15 2018 -0500

    Cleaned up environment configurations
    
    Cleaned up template to generate YAML files which pass yamllint. Also,
    added more detail to test environment for reference.

commit b7af361b802e5c33418710f5aa723c1ce07db8c1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 13 22:26:59 2018 -0500

    Updated requirements for virtualenv

commit 894a617a2e9e0535e78a00027d1e70eec81481fa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 13 22:22:28 2018 -0500

    Added initial functionality to manage environment configs

commit dd19f12a0a127a9160c69f428780a0b16c301770
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 13 22:12:57 2018 -0500

    Standardized environment configurations

commit 60cb0e83058e5a88dceeef267d685e4dba20c354
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 13 14:26:08 2018 -0500

    Tidying up prep script and group_vars functionality
    
    Centralizing prep.sh script to only need to update in one location. The
    restructure will account for this being standard. Also, added group_vars
    as a symlink like host_vars. This will provide functionality going
    forward.
    
    Added the beginning of utils.py script, that will eventually more than
    likely replace most shell script management as in Packer templates.

commit d6495fd80ed806760e913a7acf8d4a99e9bfb478
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 23:18:04 2018 -0500

    Disabled cleaning up .vagrant dirs. They are added to .gitignore

commit 6ff4cc524d4b8aabe595df56e3544ef89bc00627
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:41:27 2018 -0500

    updated for new functionality

commit 9ee725ee2fe5ee3fd394c21e864b03ff1f4b6038
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:41:16 2018 -0500

    Updated to include examples of new functionality/structure

commit 0dc7417148dc5be155cc730161d1a124b00f4df8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:40:02 2018 -0500

    Added new directory symlinks for new structure

commit 41294c3867a85cf8fa4e57d4b56abfa3f7bc1791
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:36:30 2018 -0500

    Updated prep script to accommodate new structure

commit 34e0b16efd1ac6da149c05741fe79e5f2fa46f28
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:18:55 2018 -0500

    Updated repo info based on new structure

commit 03bb7e97ee840a10bdc7978e6922582dcf86ca7e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:18:34 2018 -0500

    Added test playbook example

commit 8d413ff0410a149982b8951c7ca495b4b72e472b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:17:45 2018 -0500

    Cleaned up playbook based on new structure

commit 0724dfeaa3aab70fbe60dadcf2b492252768c7c6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:17:18 2018 -0500

    Cleaned up scripts

commit 877d4650ea245917a5358a04d16e85168d2c2df0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 12 14:15:24 2018 -0500

    Removed legacy symlinks and moved playbooks for adapting new structure

commit 26d824ce83e76989c0348219e805c4ec3e022797
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Dec 10 01:35:08 2018 -0500

    Cleaned up per shellcheck

commit 1de587486e8e33451a75f06e76b41396d9d7ef8f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Dec 10 01:34:55 2018 -0500

    Added YAML lint config file for testing

commit 8490fd95db5a23a1388e2b8e7766d6edc236ed9b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Dec 10 01:14:07 2018 -0500

    Fixed incorrect formatting

commit 695db2e890e4ba4c4017078bba1c4706c6c38f4b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 21:09:39 2018 -0500

    Cleaned up

commit b939405ca14f86402b816403f71b5c74bd603f23
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 21:07:30 2018 -0500

    Fixed incorrect path to bootstrap script

commit 855e52337709db2abfce319fee48c99800416591
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:31:57 2018 -0500

    Updated usage info based on new functionality

commit 4b17ed17e95ed370150a05e68710e5dfecf6fc76
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:30:31 2018 -0500

    Added example test script to use for new functionality

commit 7b7368234003ed1cdeef3e15ee3ee43604fc823a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:29:57 2018 -0500

    Variables updated to leverage new structure

commit 66dfeeb72bf658975801635f296ec402bcd2cbf4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:29:28 2018 -0500

    Updated to include new functionality

commit c4632fe3b5dea9fa3dad42c0601f2be01644abcc
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:28:28 2018 -0500

    Added new test environment for testing and functionality examples

commit 5534bd50cbd9fa459dc5045135c941b62ce08bd9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:27:55 2018 -0500

    Updated new environment files for new functionality

commit cddfff99c1d22dcadc4400d481cbb5b0f1e850b3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 9 20:23:36 2018 -0500

    renamed nodes.yml to environment.yml
    
    This is in preparation of future usages.

commit 0bf5eccdff0ceebdf156355a2274647e3c61f5aa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 6 11:33:23 2018 -0500

    Cleaned up to accomodate multiple provider types

commit 1e135f3b094928270f773f6e8c944e9b5701060b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 4 19:52:39 2018 -0500

    Added CentOS 5 version

commit d4cd3bd9f3e0ee0b4f5c59a7717ae4381d9847d9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 4 19:52:17 2018 -0500

    Renamed Centos folder to CentOS

commit 8c9f95526f939526ef106b8d8926e809f00eeb3e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 2 12:29:56 2018 -0500

    Trying to resolve VyOS

commit 6c3292ef50422b1637ed1b6420ed2855a6b852b5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Dec 2 01:04:07 2018 -0500

    Disabled provisioning as default

commit 2f24ce11e6c1e2ebfd816c25befdaead59c6f2d8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 1 23:53:28 2018 -0500

    Cleaned up script for future usage

commit 302a9b3ac355ff49d28c04c6dd7d7bab26213fcb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 1 23:52:54 2018 -0500

    Adjusted shared folders to include scripts and hardcode default for
    future

commit 0b62cef005ff06eac02acd967aca78d63d6bc305
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 1 23:52:19 2018 -0500

    Added Arch 2018.12.01

commit 392fda02d4dcbbe155a527f474011d83ba452bf6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 30 23:08:12 2018 -0500

    First commit of VMware support
    
    Currently works:
    - define memory
    - define cpu
    - enable 3D accelaration for desktop boxes
    - add additional disks
    
    Still needed:
    - multiple network adapters

commit 78b9f5898d88b6d122ca6f9b16c19132c4154970
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 27 01:07:57 2018 -0500

    Complete update of openSUSE

commit f6e4e80593e9df40ce6a8dc2a70f6b0b4f0feb09
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 27 00:32:04 2018 -0500

    Removed old outdated openSUSE versions

commit b0f553430b8cf2fc3461d81ac3281e38f3284776
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 26 22:35:03 2018 -0500

    Renamed openSUSE folder

commit c6507a4dce6a02032c13ae811583f960d65abc01
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 26 22:32:11 2018 -0500

    Added openSUSE Tumbleweed

commit 2008ccb37ffc4c1df117c72e57bc9f040cc4cdb3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 25 15:00:47 2018 -0500

    Added Fedora 21

commit aef8914baf0ad9ecf3421ae35e19e472749a702f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 25 00:02:26 2018 -0500

    Removed old lingering scripts

commit 4bf5d37d2f80dcdfc7361bffa2ffdc5453297a5a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Nov 24 23:48:06 2018 -0500

    Added Arch 2018.09.01

commit 2042eaec1ecf5ade7ca8aaf7eceb43b371e49d28
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 23 22:07:07 2018 -0500

    Added Arch 2018.10.01

commit a9d7f7f6f995e077a0b0e19c0f00b4ad72be2715
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 23 17:16:51 2018 -0500

    Updated Arch to new format

commit 2503234baac04504729a3f026f7af684743939b5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Nov 22 23:55:46 2018 -0500

    Reorganized VyOS 1.1.8 and added new box
    
    Virtualbox guest additions not working though

commit da2783d8c6c2bd2a93084cae57b7b58be0868784
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 21 22:31:37 2018 -0500

    Updated box names to reflect new naming

commit b94aa6650536194e2cac88ddcd6ddffe914139df
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 21 17:10:40 2018 -0500

    Added Windows 2019

commit 7ae9ec1590e708e9b868bfa85ba5b3f29cd77c48
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 21 13:00:13 2018 -0500

    Added Windows 10

commit a59dd97f3670369bba981de4a3b81f76e291f14b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 20 10:36:23 2018 -0500

    Added Windows 2016

commit fd64763424bd20976dd55e15c423a19e7b062413
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 20 01:01:42 2018 -0500

    Added new updated Windows 2012 R2 template

commit 729d6d9a5aab0afdac310e13983248c405b9c164
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 20 01:00:04 2018 -0500

    Updated to account for Windows guests.
    
    When building new Windows Packer templates I have run into an issue with
    WinRM communication which has been resolved with the WinRM settings. I
    also ran into an issue where the default virtio network driver would not
    work with VirtualBox guest additions. So, to get around this, we are
    pinning the nic_type to 82540EM which works.

commit 07ebf25d70475177d2ec7df90a842cdb87a4df1f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 20 00:59:09 2018 -0500

    Cleaned up old Windows templates

commit ec6e22ee789070c4b3303580e07782ea9fcf89ca
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 18 17:39:02 2018 -0500

    Added Linux Mint 18

commit d65796e93f7e916fae28ce9c6c174d7fd6feaf2f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 18 16:20:52 2018 -0500

    Added new versions of Alpine

commit b3e755536cb5112cb06fd1654b44d94116711950
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 18 16:20:31 2018 -0500

    Removed older versions of Alpine.

commit 2c5a453b82c54411942fadb3d6ecf7f6eacb4393
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Nov 17 22:19:10 2018 -0500

    Added Oracle Linux 7

commit 57a48a20584d20a06ddc918b99732c89a848c38a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Nov 17 01:57:07 2018 -0500

    Added Fedora 29 desktop

commit 166eacab26f06cdb6e36579a39c5e9aa76e1ff40
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 16 16:32:00 2018 -0500

    Added old Ubuntu 14.10 Utopic

commit fbb398486887f483a724059d20fa937dc8d626ad
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 16 16:27:02 2018 -0500

    Added Ubuntu 18.10 Cosmic desktop

commit 4868f62f090af32bf58b9dc2ff2ea4e4eab0d97e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 16 10:55:47 2018 -0500

    Updated to new Linux Mint 19 box

commit 35f5a956e69a21cb70a526e51a5b4eb44109c6ce
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Nov 16 10:55:27 2018 -0500

    Cleaned up old environments

commit 4b1c771e3facad0402514f7d0c59604dec27bf65
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 14 18:24:12 2018 -0500

    Added CentOS 7 Desktop

commit d64b7acfcccbc7a5a6d9604ca14fd0f3f39ca6ca
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 14 00:30:45 2018 -0500

    Added Ubuntu 18.10 Cosmic

commit fc66d738ec09b5df0d1cf5576ce3a78ec8f10b41
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 13 19:59:24 2018 -0500

    Added Debian Stretch desktop

commit 84e4b1e324f575b03a368d321fa8c1d6a933bfa8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 13 11:22:28 2018 -0500

    Added updated Ubuntu Trusty desktop version

commit 64cf18d758d7018323067a2144c629ddf1b80ce9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Nov 13 09:14:43 2018 -0500

    Added Ubuntu Xenial Desktop

commit 1e2b01659e2ec76883b24f6e1c26d7db58217405
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 12 23:42:27 2018 -0500

    Added Ubuntu 18.04 Desktop

commit a67c63a55d39e575d51b9f6ac779ef953658aece
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Nov 12 20:05:19 2018 -0500

    Reorganizing folders for better management

commit ae5509eba7c1e58e67f064c056f9e81338dbd23b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Nov 1 02:01:38 2018 -0400

    Added Fedora 29 support

commit 8ab9ab00c4ecc06479058521e76843530d984cb2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Oct 25 01:17:28 2018 -0400

    Cleaned up YAML files

commit bc90f1763d535ac9d2448a9f65c74cc3b80194f7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Oct 24 23:59:05 2018 -0400

    Added ability to use linked clones - default: true

commit 543fd3941dea2e8f7d1a7924963d50c9de47ac08
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 31 15:31:10 2018 -0400

    Added condition to only upgrade Python modules when install_ansible is true

commit f148645b2228cff00873f1e7ebf34a8f9bba3a06
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 31 15:24:06 2018 -0400

    cleaned up code

commit 3949634399507e21654752a5efc7e9ba0af388f7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 31 15:23:48 2018 -0400

    Updated Ansible version to install and also added var to define if Ansible should be installed. Default is now false.

commit d4e49aaf658be7acdc8ec29ea57dc4996a246877
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 24 14:52:39 2018 -0400

    Fixed symlink to scripts for Linux Mint 19

commit ac8aef37c0e0ccd090bca8471da337b901d65efb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 24 14:32:27 2018 -0400

    Added Linux Mint 19 box

commit 4b1657adeed7fa992b6706b9f6b4521042702e6b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon May 14 21:45:25 2018 -0400

    Disabled provisioning by default

commit 836c7a77923c4c3cde9323d2a681481d64b3631c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon May 14 21:28:13 2018 -0400

    Added Scientific Linux 7
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 2ab19983cfa680078c51d9f915c258eddd184962
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri May 4 23:50:55 2018 -0400

    Fixed scripts symlinks
    
    When copying the new distro folders I forgot to prep scripts to be a
    symlink to the scripts folder in the parent. This was implemented to
    keep scripts in a single location in order to make changes consistently
    in a single location.

commit b1e10c3850237635655b2efaf22c2620a5c47eb8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue May 1 16:31:09 2018 -0400

    Added Fedora 28

commit dbfdd923490b85a76799fa0191415c05a43d286e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Apr 26 21:59:35 2018 -0400

    Added Ubuntu 18.04 Bionic Beaver

commit 261a7d60c55ca75549d27a9d08b5570fa112095f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Apr 1 01:07:32 2018 -0400

    Updated to include 2.5 settings.

commit e5f9ec72fb9e5d50551ae2b80b1cab1f1c47955d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 21 00:36:34 2018 -0500

    Fixed cleanup.sh script path

commit ea0a9dbe17a64cf4611482b40fd42fe55207cf51
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jan 19 22:53:04 2018 -0500

    Added Distros and releases info

commit 484835eb4c2ea7c54aa2576bb0d424c9b4c87193
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jan 19 09:27:31 2018 -0500

    Added functionality to resolve Python module updates.
    
    If python pip version is an older version, the support for https was not
    functional. So now to get around that we are rescuing the failed updates
    by installing a newer version of pip.

commit 0cc1caf2f60a5d5881eaef395cd1247148437ea1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Dec 21 00:30:40 2017 -0500

    Updated Ansible configuration
    
    Updated to the latest version of ansible.cfg to include new options.

commit 759d4205ec4eb1a49346d2c0f89846db95e207c7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 13 12:33:07 2017 -0500

    Cleaned up formatting

commit 7536bbc725492ad34323d665e4171541c5acf920
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 12 17:02:00 2017 -0500

    Changed Debian/Ubuntu script function
    
    Instead of checking for specific distro version(s) I added a catch all
    for installing Python minimal.

commit ba25ef25c5db7ae8231dfb7c1676ff68cfed6db6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Dec 2 00:04:33 2017 -0500

    Added VyOS 1.1.8
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit e6c8de909c8fa314099c8520b13d91fd54d13eb0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Dec 1 18:47:37 2017 -0500

    Added OpenSUSE 42.3
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 54835eb5e92d89c7a9a0885adb17ed9de75fd894
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Nov 30 00:08:10 2017 -0500

    Added Windows 10

commit 5eb09fe0a0a39dcb94dc7a58e70bcc2424a9ee25
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 29 21:03:34 2017 -0500

    Added Windows 7

commit 1ab36c720c94e165d88a0426a0769eed0231b738
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 29 19:19:20 2017 -0500

    Added Windows 2008 R2

commit ca9f9a8c9cd039271f4cdb11b16b586d3d6e85ec
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 29 17:57:19 2017 -0500

    Changed Windows 2016 box

commit c3520a55cdad86ec512259216226f2c35706c242
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 29 15:46:52 2017 -0500

    Changed Windows 2012 R2 box
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit bbc39cf300735f8aa3f63ed4e1738684a1415b58
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 29 15:37:54 2017 -0500

    Fixed Windows black screen issue.

commit e07ed47f91f280c54de454ab13226cba811266f5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Nov 16 20:22:29 2017 -0500

    Added Fedora 27

commit cdb47e0a70bf9530e50f46fddc9a89844d65ef79
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 12 21:20:48 2017 -0500

    Added Linux Mint 18
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 2b8a09f09953958d5064869f47ff9464fa09ce53
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 12 21:20:35 2017 -0500

    Reorganized Linux Mint Folders
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 1ff1fe9d4a406f9aab00ff8c46edb635dd81d8ab
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Nov 12 14:36:26 2017 -0500

    Added Ubuntu 17.10 Server

commit 5f33490b5c6e41314715f4df1c46cfa701407c31
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 22 11:34:08 2017 -0400

    Added pyOpenSSL module to update list
    
    Resolves an issue with Ansible throws an SSL_ST_INIT error which is
    related to an outdated version of pyOpenSSL.
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f4e73b90ee9eb7db4499e56496884370981849d0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Sep 9 10:27:43 2017 -0400

    Fixed logic for executing scripts based on OS
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f165b26ab3e6de2d07890a22ad3665288900aed6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Sep 2 01:23:17 2017 -0400

    Removed lingering cleanup.sh scripts and updated prep.sh script
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4bb590d1137e411e605c5af65a0545487f2ed75e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Sep 2 01:18:22 2017 -0400

    Removed lingering bootstrap.sh files
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 0f35d5957dda9003082c447177baf95a64db53ce
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 22:11:17 2017 -0400

    Updated repo info
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f15bc1c833b71f12cbbbaae0d72a40bcaeb65776
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 22:11:04 2017 -0400

    Added new playbook for prepping host_vars for provisioning
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit aa69d58f13be39cf4fe6d666fda032ff46e4f55c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 22:10:30 2017 -0400

    Cleaned up default playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9efaf74d98a344e1a94f15df0226b064f5c7ae32
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 22:10:08 2017 -0400

    Added Windows box functionality
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 19ea79c0b13c284dff3f5d78ecf1cc4068d7802c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 22:03:30 2017 -0400

    Renamed default Ansible group
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 0cffed6a0192d0fc988780402b5e8dfd0d601e78
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 21:32:36 2017 -0400

    Added Windows and moved host_vars tasks to prep_host_vars.yml
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f454e22bde31e20b06c9b876bf59394adcc524fb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 21:31:20 2017 -0400

    Added missing prep_host_vars playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9c4c2c766d4589c8a79e0db6429e4c638566378f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 21:07:44 2017 -0400

    Updated Windows 2012 and added Windows 2016
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 34e5b5948048b4de91db91bcab86b1766c0f3c73
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 21:06:58 2017 -0400

    Updated nodes definitions
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 815fd82cc8f93fb8e5427453ee11cce16dfb532c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 1 20:20:46 2017 -0400

    Updated, added, and cleaned up scripts for cleanliness
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 72bc34b978fedae33d5082e4c9b9b1441de027e4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 24 12:39:42 2017 -0400

    Add Archlinux Support
    
    Added Archlinux support.
    
    Built from https://github.com/elasticdog/packer-arch
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 624653be3bfbd3e660a5f9f9332bcaaf0de53dd4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jul 14 01:14:17 2017 -0400

    Add Fedora 26 Release
    
    Added Fedora 26 first release.
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c5c61d59c02a389a3b8a4d73dc65b419b72fd7a8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jun 29 20:56:35 2017 -0400

    Resolves #24
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 067d13111225cc4290559eaa545edc536cb16869
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 28 23:56:11 2017 -0400

    Resolves #22
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 1d28547489654dbd303f51bfe1437c083dc8af26
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jun 28 23:31:56 2017 -0400

    Resolves #20
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 1abc61433bcbd2ae1e413250ca079f2a4b12e186
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 25 21:53:10 2017 -0400

    Used atom-beautify to cleanup code
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 748db638cddf7ad07439c51c62ed3d64f77a5d4b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 25 21:52:43 2017 -0400

    Added info on vagrant-container-templates
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 58c58404f97290485e9c8d973d0d53d62de49cbd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Jun 24 10:03:58 2017 -0400

    Resolves #18
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 158aea303707529be7aec8c6becf354d5ff61080
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 23:42:38 2017 -0400

    Regenerated TOC
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 296674293aa44d34348807d9c0ad0ac9dc58f481
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 23:40:49 2017 -0400

    Fixed header types
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4f5314ba0b1a501c7fc8e3c592c658044d952f16
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 23:38:41 2017 -0400

    Resolves #14
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 729dfdad6e7a79636a1f10c3ca574a760b23fc68
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 20:32:09 2017 -0400

    Added example of local dev environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c8d5871f4c1c9c2b6025d9648004ad4b8671a8ee
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 20:27:26 2017 -0400

    Resolves #11
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 3454889b7155586a2a027cfa0340c84620d45b8a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 23 17:03:27 2017 -0400

    Resolves #9
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit a1b1cb36897d8e9b72659c096d6905bc71ce31fa
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jun 13 00:41:31 2017 -0400

    Cleaned up incorrect bootstrap.bat and lingering hosts in root folder
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 38afa3b2b8a67da07e177f636502f8c985ee9892
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 18:10:09 2017 -0400

    Fixed formatting
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 6b25a15366799f9d61f3fda08254fa32fd6adc80
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 18:09:44 2017 -0400

    Fixed formatting
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 17971d3ca6f0d26cd7261dd247086e4ce64bdf60
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:11 2017 -0400

    Added missing files for desktop
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 6ecaaa404db742bc2ed9be8d2b73ab5e548dba82
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:36 2017 -0400

    Cleaned up node definitions
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 3e57418ff9269616a92dd3b608ad277763f3a677
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:25 2017 -0400

    Updated repo info
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4899ca072a291d560b37e7c1efd30408b5090098
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:36 2017 -0400

    Cleaned up node definitions
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit a90fd7e77bd6000d7b96856c9ae09a049a50efbf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:25 2017 -0400

    Updated repo info
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c63c42e8484cf56f5d4bff08661a9a091df80c15
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:58:11 2017 -0400

    Added missing files for desktop
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 28f82bfad0ce8191bafdb34004886232475af8ec
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Jun 11 17:52:35 2017 -0400

    Addresses issue #6
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c5de7c6d7ad8fac05459a75ef2d364bdab8b22d3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 9 01:29:38 2017 -0400

    Fixed missing hosts file
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 947db11db5dbce7ae8caf7831aed1806878ae508
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Jun 9 01:25:17 2017 -0400

    cleaned up bootstrap script for efficiency
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c719cf99dbd439a560dd6a04c8f3de323a9ec7e6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 3 22:05:39 2017 -0400

    Added force of symlink for hosts
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 94add07de239b7eb247c53b0f8d16c3674756b6c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 3 22:05:22 2017 -0400

    Updated for Alpine provisioning
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 66bd9451b0d256aa64274558bd455b8a7423122d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed May 3 22:04:25 2017 -0400

    Fixed Alpine templates
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit ea64f4adc7bfd8f63cd077c925ab1817a13587a8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Apr 20 01:15:27 2017 -0400

    Added missing hosts symlink for Ansible
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 0f775759893bdb655dfbc6a528ea3c4b5925d787
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Apr 19 09:52:46 2017 -0400

    Changed provisioning of nodes variablization
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 3316e2e999f762b113a082782d22cf3c1e474f58
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Apr 14 01:19:26 2017 -0400

    Changed Zesty box
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 49a576b8126e9e460a09f719cbf807525099a3de
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Apr 5 23:01:34 2017 -0400

    Updated formatting and tasks for cleaner code
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c5f543159e537e1ff555ebf30849d107be6f3110
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sat Apr 1 01:18:12 2017 -0400

    Changed Fedora 25 box
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 78a2e3c0bea1bc90f63a49bdb32d9b0f9c6b498f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Feb 26 12:43:12 2017 -0500

    Fixed host_vars updates
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c27b1ea9b6c74b61c9b89c116a77027d548f09ec
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Feb 17 20:05:04 2017 -0500

    Fixed issue with Debian not updating SSH Port
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9cc2fdeb21adc060b24e057beab14e64da74da6a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Feb 8 00:20:25 2017 -0500

    Added back my personal boxes after fixing and updating
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 691d8b15ae75056478af608c402796069882c56a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 13:05:05 2017 -0500

    Changed to Ubuntu official boxes
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit a155601a8a798c3766d4dff4df7e2204d5941b93
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 13:04:46 2017 -0500

    Added info to use rsync if not using guest additions
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 830c26ad96aa2d10e5b595115afabfdd0acf7d2a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 13:04:19 2017 -0500

    Updated ignore files
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 32e73c7b62081813590e54994cfddeb94284ce3c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 13:04:04 2017 -0500

    Updated ansible config to include all options
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 249e5b587fbde208815045fb27f7ea53fe86ab41
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 13:03:32 2017 -0500

    Added Fedora 25
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit bdf692911213e7446bdc9415477720c8c1c35994
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 09:23:04 2017 -0500

    Updated for ubuntu zesty
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 1afaf6076d57ded05fecdbccc8052b92bfce55cb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 09:22:22 2017 -0500

    Updated for Ubuntu Zesty
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9fbc7db451c97bc73b9a86a20821b4f94a0e79c4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 01:22:57 2017 -0500

    Cleaned up code
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit b0bcf4fc54692dbf232b61fa05064552ef3627fd
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jan 31 01:13:11 2017 -0500

    Fixed desktop boxes...
    GUI was not starting...Had to re-order logic
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 67b328a548188563120102a3f1b2a822809932d2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jan 30 22:55:33 2017 -0500

    Disabled provisioning by default
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c93d7b38ab7ad549f39cb160858df844d033bd28
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jan 30 22:54:30 2017 -0500

    Completely rewritten to use nodes.yml and consistent provisioning files
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit b5086a4fdb99e70470f64f3b45c0ba507a45ffe1
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jan 26 00:53:54 2017 -0500

    Updated Ansible version to install
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 8390038f56a8fe8f9ba76c17863acd7d7e14cc52
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Thu Jan 26 00:53:40 2017 -0500

    Added FreeBSD
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 536ca91976b8a9bc3388392dac8bcec654381f81
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Nov 23 18:16:22 2016 -0500

    Added Windows cleanup script
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit b6018157a9c51ef1b815b1838d032b58febedbc7
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Oct 14 22:20:44 2016 -0400

    Added Ubuntu 16.10
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 09bc393978ca714004fb5b80ab723dca66bb0d6a
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Oct 11 11:37:33 2016 -0400

    Addresses issue #1
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit b8c10c129f98810398e2f25f73d081cf32c647a6
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Aug 26 22:52:46 2016 -0400

    Updated Vagrantfile templates
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit e157be70323ca3d5574a5d6170b17b4653412b61
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Jul 6 19:58:39 2016 -0400

    Added Fedora 24
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit e06a93919ff0dd518057ecca556689ce6f5be185
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Jul 5 11:47:34 2016 -0400

    Added Xenial check
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 322aac8fafe684ba824251a54a4879974593c466
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:29:31 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit c074d58b2a854b562760d97e06909b7afb0a4300
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:28:25 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit bc1cc2dd47a869c907172d5c18dfc7096a7af4cb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:26:22 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 34bcb5e83d64f67bfeb190d2b5a58813c2a59a9b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:26:14 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 6db680c8658bffe81517ac7bf64a225386a9862e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:15:47 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit eadcde29d836b2d7b3bbf57425605a18c2be86f9
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:15:38 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9107282e23dd89020ad36601a4cede486d34ec2b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:14:06 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 9fdb0e0e35e37193efa402e551b764bb1378ecc2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:13:29 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 65bb072b501fae4e3e7a70e4f99a8d3c2ba083b4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:11:24 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4b3c4abb1eb741537080325bec614bdafc8b923d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:09:56 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 649d8264202a2856cf0d64ad399bfb8a993ad7ad
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:09:39 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 18e5716cdbd51ecbea1cbb2377e98720fbe11055
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:09:31 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 6593bffee454b4083108fc219c206d526d536476
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:06:26 2016 -0400

    Added git ignore
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 832725c3af0b3a7bd5ec3629cfe71d4088dfc4b4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Jul 4 01:06:16 2016 -0400

    Updated Vagrant environment
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 6500a642bbd33971cd950e8ac919a10276563884
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Fri May 6 09:13:59 2016 -0400

    Updated for OpenSuse
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit f5893feffd7eefa693d9b1d4e7f2228c3e2b3e5b
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Thu May 5 23:06:29 2016 -0400

    Centralized bootstrap script and playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit a2c3ab5e701562819c143d8a096e109191e236b7
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Thu May 5 23:03:14 2016 -0400

    Added OpenSuse
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 9e0be60f917c168a02463a85287e30dca2be83a8
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Thu May 5 23:00:17 2016 -0400

    Updated Vagrant environments
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit d06cf954e35594da7ff30d6753d69f0cc9f41d2b
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Tue May 3 23:14:41 2016 -0400

    Updated Vagrantfile to latest
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit fd1a8a5fb3c27e605e70424a137482b665181df1
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Tue May 3 23:05:21 2016 -0400

    Disabled provisionioning default
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 813ec6090f79aca3ae89d2b9544468e1e835b326
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Tue May 3 22:53:08 2016 -0400

    Fixed RedHat,Debian based Ansible installs
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 2aeae97094b006d7170ad992757a5f25527cd477
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Tue May 3 17:35:41 2016 -0400

    Centralized bootstrap script and playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 6c4fc7e416005dca665dbe776d381fbf9a4e35d2
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Fri Apr 29 00:44:10 2016 -0400

    Added Ubuntu 16.04
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 18820ba27e15fc42f34137290073918d2af7f4eb
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Sat Mar 5 00:12:47 2016 -0500

    Updated Vagrant Build
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 0cd2c723bfa0d9531d6edc5bd4aadec3a74cb101
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Fri Mar 4 10:44:19 2016 -0500

    Made shell scripts executable
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit cb75b1c7b22833a12a435b28b60b7ec2f1ab03ab
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Fri Mar 4 10:21:08 2016 -0500

    Updated OS detection script
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit c6fca10e235d5cc0af8e6fa39a477ac3d375a34b
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 19:47:16 2016 -0500

    Updated playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 95a10d4cf0adce6293bbc2ef77e6babfd38ae0ae
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 19:46:02 2016 -0500

    Updated playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit fe5ab78dca95d787413df88d0c97f4ae7dbd3e4c
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:56:03 2016 -0500

    Added options to upgrade packages
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 5d1f121f61f2276a9e362dafd04520345c2670f8
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:48:54 2016 -0500

    Updated Repo Info
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 9b86c012ad757e474c3016094194db5b2aa2d213
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:21:51 2016 -0500

    Cleaned up
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 3d5af615305aaf8ecddcfdd984473c8129d7d647
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:17:39 2016 -0500

    Fixed OS detection
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit e0262395cb5069fedc3734b9cf38bdd479928053
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:15:00 2016 -0500

    Made script executable
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 1ea306c865c40e343b4e321199966e7de6afe98a
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 17:11:58 2016 -0500

    Fixed OS detection
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 6af06df14dc719295d6d1f4cba67ef278f08a2d4
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 16:39:36 2016 -0500

    Added Fedora 22
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 7f0a70669c7cec3ab6d34705f32860bb37a6f2bf
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 16:25:29 2016 -0500

    Made script executable
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 572d7fd2adc1d2390666256fb3df487ed018f75f
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 16:24:26 2016 -0500

    Cleaned up
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 5e0be1d8d9a83ec4fca8686895c296744fe943ac
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 16:23:21 2016 -0500

    Cleaned up
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit fd30cedf873e1ceb2f74ff2f8c7537e5336699e9
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:54:10 2016 -0500

    Added Fedora 23
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit ac2eb1c60c17797f19ba616a6ef8d170c301ee30
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:53:27 2016 -0500

    Removed old 22
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 70d2770261847c2aa09a15e7c9625cd679d86728
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:48:02 2016 -0500

    Reorganized CentOS 7
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit ad9abc1cb7028e167de013ccbfbf437eb07e4b23
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:47:46 2016 -0500

    Changed CentOS 7
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit afce715f7095180a09427949119e6c1473c84e89
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:47:10 2016 -0500

    Added CentOS 6
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 29015b3a47ead349f3ea480fe2fbb28484db7834
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:46:51 2016 -0500

    Removed 6.5
    
    Replaced with 6 in general
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit caed48b1c43196f137b69da0d69e037180f784cd
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:39:19 2016 -0500

    Updated Windows box
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 611fcd352d02241bb3ce79d5ba239e781fbb55aa
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 15:38:46 2016 -0500

    Fixed box name
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit eaf0e305ddf333a5e87b4fcdaacf7fefef8ae80e
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:38:19 2016 -0500

    Added Wily64
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit f40bb89dbddaf0a13ce31ac74e9811c402f8baa9
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:30:15 2016 -0500

    Added Vivid64
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 71650953509972d49ee0b303acf2c51202047ea4
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:26:47 2016 -0500

    Added Precise64
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 32a83811ab4446c32f69e62618d3d62c937a38ca
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:25:04 2016 -0500

    Updated Vagrant build
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 82db5431cc35991625ef043ab4c890438a4df495
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:21:44 2016 -0500

    Added Debian Wheezy
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 01e9bd127672703a4a211643079579fb05bfb982
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:15:19 2016 -0500

    Made script executable
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 0a380276a93bed86ad7e1d1e02a399e8eadf65bf
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Wed Mar 2 11:13:16 2016 -0500

    Updated Vagrant build
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 8f967a4c2d3e23744b44325362dfe3192ee3e87f
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Sun Feb 21 23:16:31 2016 -0500

    Fixed umount
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 7768a1f88e31a72b8bd3c8ec812cfcf9f93c7110
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Sun Feb 21 23:13:50 2016 -0500

    Cleaned up playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 1bafda8763b209d4de70debccb0f4d54e32d6a4b
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Sun Feb 21 23:01:37 2016 -0500

    Change ansible version and playbook
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 8e9c412605ddae06e590fb6ead59072cd38b21ea
Author: Larry Smith Jr <mrlesmithjr@gmail.coml>
Date:   Sat Feb 6 22:31:26 2016 -0500

    Added Alpine
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.coml>

commit 0d0d2aac842d50fef8cd918f5680d810991b7c80
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Wed Dec 30 21:20:22 2015 -0500

    Added Debian Jessie Desktop w/Gnome
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 4d9852cb8232577c4729cdb4a180e938693b7069
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 19:07:50 2015 -0500

    Updated for Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit dc381f15a372368eb9a90b7c98043c4104a6d2f0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 18:57:28 2015 -0500

    Removed state for easy_install
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 8b65230cd78e693c641834f4758b488953218a40
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 18:52:50 2015 -0500

    Updated for Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 3a9a183e042ed92f1a852a8197eb94e654ec80af
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 18:00:00 2015 -0500

    Updated for Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 692b8d9c2f80c4b40b35db230adbc766ac216d54
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 16:37:02 2015 -0500

    removed host_vars
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 54fc371df7f2a429b76f050e636675eca1ed1091
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 16:31:41 2015 -0500

    Updated and cleaned up
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 59829845f0db631749046ac382d2b797b16749d8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 16:12:35 2015 -0500

    updated for Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 132375acca2df2eb445ea7aadae5713eb6b79024
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 15:33:22 2015 -0500

    modifying script for Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit f39b6813931913dfa0ea4697a89129990e566a1f
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Dec 29 15:30:18 2015 -0500

    Added Debian
    
    Signed-off-by: Larry Smith Jr <mrlesmithjr@gmail.com>

commit 0b88b300f1429c398ea5b27f8e38a1a52c573754
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Tue Oct 6 21:23:58 2015 -0400

    added Windows Host OS detection to Vagrantfile

commit 524d0faf3e896688a8eb4e40bd45142b7bb37222
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Sep 28 10:24:35 2015 -0400

    Ubuntu guest additions install is erring

commit 9c4194da71eeaf741e3ebc73d3c623ad393aeb77
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Sep 28 08:36:53 2015 -0400

    Added Ubuntu Trsuty64

commit c043daa1bb2ed13c0fb5d5f3f87849a83d281861
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Mon Sep 28 07:12:50 2015 -0400

    added symlink for ansible hosts inventory

commit f1e259bdaec219fed03e83efb2f70dbb4ca0b60c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 22:41:29 2015 -0400

    added additional pre-reqs

commit 8abac08539a20c8884e1cc1be8266551c1cac150
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 22:33:44 2015 -0400

    made script executable

commit 6e354d3a575d4499d2642e448da5a1d31f0b1cfb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 22:32:42 2015 -0400

    Added CentOS

commit 5c14d2df6bd69186465ecfaa616f06b5b989b85d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 22:08:42 2015 -0400

    changed packager to dnf and removed epel repo

commit 8355de1688e9cff58233ee32897c0694e2c41fbf
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 22:04:37 2015 -0400

    changed final cleanup script for bash history

commit 29f53b2a9244151ecfd61792b9b48f87328ede3d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 20:18:21 2015 -0400

    updated meta

commit ad94c69712916868b42b753d2365defa52d73ebe
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 20:12:26 2015 -0400

    added Fedora22 Server

commit eceaebfa2efb1862e701da79efee1c4b35f66fd0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 19:21:42 2015 -0400

    made script executable

commit d580d02855191546be3e1faa8729853e1d40afba
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 19:14:58 2015 -0400

    disabled selinux

commit cdbcaefbbb6f9b5554d0306ecd6edf79739b3656
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 19:11:03 2015 -0400

    cleaning up playbook

commit 6bfd88ee2b49af75933c2d88fdf57258ccf73e93
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 19:08:25 2015 -0400

    trying to fix virtualbox driver install

commit 1799d68145cec8e0f414808b08988cf2d23d1e21
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 18:53:30 2015 -0400

    added missing packages and reorganized

commit 397eb1d76dbb958eb6219126d0e3d7e5299b7db5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 18:32:08 2015 -0400

    fixed auto install switch

commit 74140fe2e563f99bfb3e9defd312e1f6c86863d4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Sun Sep 27 18:30:04 2015 -0400

    adding fedora 22

commit cbd6450d1c5714e7d9f268235d033ad627eb6d5b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 22:33:42 2015 -0400

    added windows 2012 r2

commit 2d16ec46c1db4df9ba119abc6e539cbc76243b2b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 18:38:33 2015 -0400

    merged history into one command

commit 8143043590f99f759599e0737e3bea9128c77ced
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:59:16 2015 -0400

    trying to fix cleanup

commit 35afa77ccc1874673c17d0b130777d90e9257fd4
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:55:47 2015 -0400

    fixed history cleaning

commit 710d0521e532e9f61c1594fb261dae8d6a9e3d19
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:50:14 2015 -0400

    added sleep and cleaned up redundant commands

commit 3387379a680f5233b9548087dcf5660c9415f29b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:45:34 2015 -0400

    added cleanup playbook

commit 3c482eaef9e52fcd0c1108fcd5f3139dbd942bd0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:36:33 2015 -0400

    added reboot to the end of script

commit 5f4ed3763dee1e31be92218cb07be471fe23e12c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 17:25:31 2015 -0400

    added trusty64 unity

commit 6eec58d7fca4ad3fefea753c68162f9c077cdf10
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 16:36:58 2015 -0400

    added trusty64-desktop-unity

commit d36e748d23aea34bbd5a338ba464b7ba37f7afeb
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 16:16:46 2015 -0400

    disabling symlink task
    
    Causing VirtualBox Kernel to not work?

commit 9cfa603a456e9e49b1159083fe44901a0b4b5af2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 16:10:13 2015 -0400

    added comments and Clear bash history

commit 63afb922e300bd86bcaac05ee91be989ef0f105e
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 16:03:21 2015 -0400

    moving zeroing out space out of Ansible

commit b279a8ea82f1819ece09a98b097b491c1b6c10e3
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:40:55 2015 -0400

    trying to fix cleaning up space

commit ba2493ad4860515227aadd2490f5113e759f69ed
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:34:45 2015 -0400

    added pause for time to clean up space

commit d568a5e4bb57681493e2200c3b48c15289a495df
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:30:33 2015 -0400

    fixing errors on running out of space

commit a8b9aa1738c3cb8acb4a80c5891a899d9e1ca6ae
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:24:38 2015 -0400

    fixed error from second run

commit b10d002b5979c6af91d6904b4a4825081536867d
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:21:35 2015 -0400

    fixing out of space error during zeroing out space

commit d7b3316b75e20d78a544d1739dfe04e4ab70b1c8
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 15:18:12 2015 -0400

    fixing virtualboxadditions version

commit 11255a5eac36eed60ab1b18918ef2adf0507afad
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:53:55 2015 -0400

    fixed password hash

commit 89da798caf373d01d803f7660dc4f8ebc5895f64
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:50:11 2015 -0400

    fixed mount task

commit 9319fef76d9315ea83adc855ca622eadf69a50d2
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:39:41 2015 -0400

    added prompt for sudo password

commit bc5b00afe16709a825e45c4b267aeb2f2513a5f0
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:37:21 2015 -0400

    commented out vars_files parameter

commit aa2aa90a913934302564708700ed052858f3a923
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:36:20 2015 -0400

    fixed missing quotes

commit 6add2bf143526a1b291e98273264cb7f4350457c
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:35:23 2015 -0400

    fixed missing with_items

commit c54c486b02064650407cf85229fc5fbff9196607
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:34:27 2015 -0400

    fixing for localhost execution

commit 46c22ad734798437d028f8996bdb262e98a01de5
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:32:50 2015 -0400

    fixing playbook

commit 47400a48a93ae6bcce4a48d9d2f609f53bdfbd77
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:29:07 2015 -0400

    made shell scripts executable

commit af0a0f9bf6aca83d43379cae6efd4564cd0a8801
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 14:27:18 2015 -0400

    converting shell script to ansible playbook

commit bd0162e19a7a9cf5311119ba2dc047d07bb73479
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 12:56:18 2015 -0400

    added openssl-server

commit 268d8b03a51341d5ae69d4fcad68a0793a8da953
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 12:49:53 2015 -0400

    added scripts and reorganized folders/files

commit eb018090c4b627f8d72b893af2d4508f5fb81f7b
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 12:14:01 2015 -0400

    updated meta

commit b7f38c48090f1a67afb7f75644996875a7796c23
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 12:10:30 2015 -0400

    updated meta

commit d3c4e78b5d54529500fec8b5151041cc9dcfb537
Author: Larry Smith Jr <mrlesmithjr@gmail.com>
Date:   Fri Sep 18 12:06:00 2015 -0400

    first commit
