# -*- coding: utf-8 -*-
import io
s=io.open('tree.html',encoding='utf-8').read()
s='<!doctype html>\n<html lang="ru" data-theme="light">\n<head>\n<meta charset="utf-8">\n'+s
s=s.replace('<div class="wrap">','</head>\n<body>\n<div class="wrap">',1)
s=s.replace('<details class="person','<details open class="person')
s=s.replace('Нажмите на человека, чтобы открыть справку.','Справки о каждом человеке — на следующих страницах.')
io.open('pdf-source/tree-print.html','w',encoding='utf-8').write(s)
