#!/bin/bash

echo ''
echo '###################'
echo 'TESTING INDEX...'
echo '###################'
curl http://localhost:80/index.html
echo ''

echo ''
echo '###################'
echo 'TESTING PUBLIC...'
echo '###################'
curl http://localhost:80/css/test.css
echo ''
curl http://localhost:80/js/test.js
echo ''
curl http://localhost:80/img/test.jpg
echo ''

echo ''
echo '###################'
echo 'TESTING UPLOADS...'
echo '###################'
curl http://localhost:80/uploads/test.jpg
echo ''

echo ''
echo '###################'
echo 'TESTING 404...'
echo '###################'
curl http://localhost:80/uploads/test
echo ''

echo ''
echo '###################'
echo 'LOCAL LOG...'
echo '###################'
cat /home/box/test.error.log
echo ''

echo ''
