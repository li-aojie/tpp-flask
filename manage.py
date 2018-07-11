# 引入flask基础模块
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from tpp import create_app

from tpp.exts import db
# --------------------------------------------------------------
# 将需要迁移目的模型类导入
from tpp.models import Movie, Cinema, Hall, HallSchedule, User, Seat, Order, SeatSchedule

# 创建项目实例
app = create_app()

# 迁移管理对象
migrate = Migrate(app, db)
# 创建管理对象
manager = Manager(app)
# 添加db命令
manager.add_command('db', MigrateCommand)
if __name__ == '__main__':
    manager.run()