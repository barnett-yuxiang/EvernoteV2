import fs from 'fs';
import { compile } from 'svelte/compiler';

// 读取 Svelte 组件文件
const input = fs.readFileSync('src/App.svelte', 'utf-8');

// 编译 Svelte 组件
const { js } = compile(input, {
  filename: 'App.svelte',
  generate: 'dom',
  format: 'esm'
});

// 输出编译后的 JavaScript 代码
console.log(js.code);
