Sublime Text 3 Settings
=======================
My personal settings for sublime text 3.


Setup
=====
In order for these settings to work, you need to install some other sublime packages. This can be automated by executing the python script `AddPackages.py`. However, **this requires you to have [Package Control](https://packagecontrol.io/) installed.**

If you have python installed, do the following:

(Windows)
```batch
py -3 AddPackages.py
```

(Other)
```bash
./AddPackages.py
```

It doesn't matter in which directory you execute this script.

If you want to manually install those packages, open the `AddPackages.py` file and check the value of the `extraPackages`.
