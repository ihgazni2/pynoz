pip3 uninstall pynoz
git rm -r dist
git rm -r build
git rm -r pynoz.egg-info
rm -r dist
rm -r build
rm -r pynoz.egg-info
git add .
git commit -m "remove old build"

