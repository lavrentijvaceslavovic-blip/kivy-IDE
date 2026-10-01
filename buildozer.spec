[app]

# Название твоего приложения
title = Kivy IDE
package.name = kivyide
package.domain = org.kivy

# Путь к исходному коду (где лежит main.py)
source.dir = .
source.exts = py,png,jpg,kv,atlas

# Зависимости (убедись, что python3 и kivy на месте)
requirements = python3,kivy

# Ориентация экрана (portrait — вертикальная, landscape — горизонтальная)
orientation = portrait

# Разрешения (если твоему приложению нужно читать/писать файлы)
android.permissions = WRITE_EXTERNAL_STORAGE,READ_EXTERNAL_STORAGE

[buildozer]
log_level = 2
warn_on_root = 1
