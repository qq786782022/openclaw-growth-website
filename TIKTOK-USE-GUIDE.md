# TikTok播放器使用说明

## 🎵 功能介绍

在成长网站中添加了TikTok网页版板块，可以：
- 📱 直接访问TikTok网页版
- 🌐 响应式设计，支持手机/平板/电脑
- ⚡ 优化加载速度，流畅体验

## 📋 使用步骤

### 1. 连接代理节点

TikTok和YouTube一样，需要连接代理节点才能正常访问：

**Android设备（Clash）**:
```
1. 下载Clash for Android
2. 导入配置: https://github.com/qq786782022/openclaw-backups/raw/master/skills/custom/tools/clash-config.yaml
3. 选择VLESS或Trojan节点
4. 点击"连接"按钮
```

**iOS设备**:
```
1. 下载Shadowrocket或Quantumult X
2. 添加节点配置
3. 连接TikTok订阅（见下方）
```

**电脑（Windows/Mac）**:
```
1. 使用ClashX或Clash Verge
2. 导入Clash配置文件
3. 连接节点后访问网站
```

### 2. 访问TikTok播放器

**方式1 - 网站内播放器**:
```
访问: https://qq786782022.github.io/openclaw-growth-website/

点击导航栏: "🎵 TikTok"
```

**方式2 - 直接访问TikTok**:
```
直接打开: https://www.tiktok.com
```

### 3. 测试节点连接

如果TikTok无法加载，检查：
- ✅ 代理节点已连接
- ✅ 网络正常
- ✅ 浏览器允许加载iframe

## 🎯 V2Ray节点信息

**服务器**:
- IP: 47.85.49.105
- 端口: 10086-10089
- UUID: 7d9285ae-ccef-4f19-956a-a78eeb8b0b5f

**订阅链接**:

**VLESS** (推荐):
```
vless://7d9285ae-ccef-4f19-956a-a78eeb8b0b5f@47.85.49.105:10086?encryption=none&type=tcp&security=none&sniffing=none#VLESS-47.85.49.105
```

**VMess**:
```
vmess://7d9285ae-ccef-4f19-956a-a78eeb8b0b5f@47.85.49.105:10087?network=tcp&security=none&alterId=0&uuid=7d9285ae-ccef-4f19-956a-a78eeb8b0b5f#VMess-47.85.49.105
```

**Trojan**:
```
trojan://7d9285ae-ccef-4f19-956a-a78eeb8b0b5f@47.85.49.105:10088?security=tls&sni=www.google.com&type=tcp#Trojan-47.85.49.105
```

## 🎨 网站特色

- ✅ **响应式设计**: 完美适配所有屏幕尺寸
- ✅ **快速加载**: 优化了加载速度
- ✅ **安全访问**: 通过代理节点安全访问
- ✅ **完整功能**: 支持所有TikTok网页版功能

## ⚠️ 注意事项

1. **网络要求**: 必须连接代理节点才能访问TikTok
2. **浏览器支持**: 推荐使用Chrome、Firefox、Safari等现代浏览器
3. **防火墙**: 部分网络可能需要额外配置
4. **内容安全**: TikTok内容符合当地法律法规

## 🔧 故障排除

**问题1: TikTok无法加载**
```
解决方案:
1. 检查代理节点是否已连接
2. 尝试切换不同的节点（VLESS/VMess/Trojan）
3. 清除浏览器缓存后重试
```

**问题2: 页面加载缓慢**
```
解决方案:
1. 切换到延迟更低的节点
2. 关闭其他网络应用
3. 使用5G或WiFi网络
```

**问题3: 无法播放视频**
```
解决方案:
1. 检查代理节点是否稳定
2. 刷新页面
3. 切换节点后重试
```

## 📞 支持

如有问题，可以：
- 查看 GitHub Issues: https://github.com/qq786782022/openclaw-backups/issues
- 检查V2Ray服务状态
- 重新导入配置文件

---

**更新时间**: 2026-02-18
**版本**: v1.0
**状态**: ✅ 已部署完成
