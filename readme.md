las funciones utiles estan en el archivo de adminn.py

opciones 

```
-f  =firefox
-g  =chrome
-H  =navegador headless
```

tienes que agregar geckodriver o chromiumdriver, segun tu proyecto, gecko me corrio bien en ubuntu pero no en raspberry
chromium corrio en raspberry pero npo en ubuntu


descargar geckodriver actualizado para usarlo en ubuntu, descargar y descomprimir:

```
chmod +x geckodriver
export PATH=$PATH:/path.../geckodriver y agregarlo como variable al driver
o guardarlo en /usr/bin/
```

lo mismo con chromium en raspberry

xpath se puso raro muy rapido
```py
button__mac=driver.find_element_by_xpath("//div[@id='blocked-devices']//table[@class='data']//tbody//*//td[text()='"+val_ip_td+"']//..//td[5]")
```

`//*` nos deja elegir cualquier item de ese nivel
`//..` es para el padre de un item, tambien esta parent, sibling y mas pero no los cheque 
`//td[5]` nos deja elegir por numero directamente en una lista de tags
`//td[text()='texto_1']` busca el texto dentro de una etiqueta `<td>texto_1</td>`
`/td[text()='"+val_ip_td+"']` es para pasar variables de python al string