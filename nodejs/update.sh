pm2 stop web
pm2 stop main
git pull
npm run build
pm2 start npm --name web -- start
cd ..web
pm2 start main.py
