hexo clean && hexo g
cp -r ./public/* ./.deploy_git/

pushd .deploy_git/
git add .
git commit -m "$(date)"
git push
popd