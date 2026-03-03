
const fs = require('fs');

// 读取源配置文件
const srcApi = JSON.parse(fs.readFileSync('../api.json', 'utf8'));
// 读取目标配置文件
const api = JSON.parse(fs.readFileSync('../TVBoxOSC/tvbox/api.json', 'utf8'));

// 替换指定属性
api.lives = srcApi.lives;
api.parses = srcApi.parses;
api.ads = srcApi.ads;

// 写入更新后的配置
fs.writeFileSync('tvbox/api.json', JSON.stringify(api, null, 2));

console.log('Configuration updated successfully');
