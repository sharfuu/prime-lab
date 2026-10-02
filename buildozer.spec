[app]

title = Prime Lab
package.name = primelab
package.domain = org.primelab

source.dir = .
source.include_exts = py,png,jpg,jpeg,kv,atlas,ttf

version = 1.2

requirements = python3==3.13.11,hostpython3==3.13.11,kivy

android.api = 35
android.minapi = 23
android.ndk = 27c
android.accept_sdk_license = True

p4a.branch = develop
p4a.commit = d2ee8c5

orientation = portrait
fullscreen = 0

[buildozer]

log_level = 2
warn_on_root = 1