from practice3 import Restaurant as R
from Admin import Admin

anthony = R("Anthony's pizza", "Italian")
anthony.describe_restaurant()


admin = Admin("adder", "minmin", 0)
admin.greet_user()
admin.priv.show_privileges()


