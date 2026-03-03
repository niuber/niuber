
const fs = require('fs');
const path = require('path');

// 获取当前工作目录下的文件路径
const srcApiPath = path.join(__dirname, 'api.json');
console.log('srcApiPath',srcApiPath);
const targetApiPath = path.join(__dirname, 'TVBoxOSC', 'api.json');
console.log('targetApiPath',targetApiPath);

try {
    // 读取源配置文件
    const srcApi = JSON.parse(fs.readFileSync(srcApiPath, 'utf8'));
    //console.log('srcApi',srcApi);
    // 读取目标配置文件
    const api = JSON.parse(fs.readFileSync(targetApiPath, 'utf8'));
    //console.log('api',api);

    // 替换指定属性
    api.lives = srcApi.lives;
    api.parses = srcApi.parses;
    api.ads = srcApi.ads;

    // 写入更新后的配置
    fs.writeFileSync(targetApiPath, JSON.stringify(api, null, 2));

    console.log('Configuration updated successfully');
} catch (error) {
    console.error('Error updating configuration:', error.message);
    process.exit(1);
}
