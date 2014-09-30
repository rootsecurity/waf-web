# !/usr/bin/env python
#-*- coding: utf-8 -*-
#=============================================================================
#     FileName: atk_type.py
#         Desc:
#       Author: 苦咖啡
#        Email: voilet@qq.com
#     HomePage: http://blog.kukafei520.net
#      Version: 0.0.1
#   LastChange: 2014-09-30
#      History: 
#=============================================================================
atk={
    "(?:(?:current_)user|database|schema|connection_id)\s*\(": "敏感目录",
    "(?:(union(.*?)select))": "sql注入",
    "(?:define|eval|file_get_contents|include|require|require_once|shell_exec|phpinfo|system|passthru|preg_\w+|execute|echo|print|print_r|var_dump|(fp)open|alert|showmodaldialog)\(": "本地文件包含",
    "(?:etc\/\W*passwd)": "敏感目录",
    "(?:from\W+information_schema\W)": "sql注入",
    "(gopher|doc|php|glob|file|phar|zlib|ftp|ldap|dict|ogg|data)\:\/": "敏感目录",
    "(onmouseover|onerror|onload)\=": "xss攻击",
    "(phpmyadmin|jmx-console|jmxinvokerservlet)": "敏感目录",
    "(vhost|bbs|host|wwwroot|www|site|root|hytop|flashfxp).*.rar": "敏感文件访问",
    "/(attachments|upimg|images|css|uploadfiles|html|uploads|templets|static|template|data|inc|forumdata|upload|includes|cache|avatar)/(\\w+).(php|jsp)": "文件上传",
    "\$\{": "",
    "\$_(GET|post|cookie|files|session|env|phplib|GLOBALS|SERVER)\[": "0day/溢出攻击",
    "\.(bak|inc|old|mdb|sql|backup|java|class)$": "敏感文件访问",
    "\.(svn|htaccess|bash_history)": "敏感文件访问",
    "\.\./": "任意代码执行漏洞",
    "\:\$": "任意代码执行漏洞",
    "\<(iframe|script|body|img|layer|div|meta|style|base|object|input)": "xss攻击",
    "base64_decode\(": "xss攻击",
    "benchmark\((.*)\,(.*)\)": "敏感文件访问",
    "group\s+by.+\(": "sql注入",
    "having|rongjitest": "sql注入",
    "into(\s+)+(?:dump|out)file\s*": "本地文件包含",
    "java\.lang": "敏感文件访问",
    "select.+(from|limit)": "sql注入",
    "sleep\((\s*)(\d*)(\s*)\)": "sql注入",
    "xwork.MethodAccessor": "敏感文件访问",
    "xwork\.MethodAccessor": "敏感文件访问",
    "(HTTrack|harvest|audit|dirbuster|pangolin|nmap|sqln|-scan|hydra|Parser|libwww|BBBike|sqlmap|w3af|owasp|Nikto|fimap|havij|PycURL|zmeu|BabyKrokodil|netsparker|httperf|bench)": "扫描器扫描"
}