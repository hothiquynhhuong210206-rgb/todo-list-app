
tasks = []
def add_task(task_name):
    """Thêm một công việc mới vào danh sách"""
    tasks.append(task_name)

    print(f"đã thêm công việc:{task_name}")

#--Điểm bắt đầu của chương trình
if __name__ == "__main__":
    print("Chào mừng bạn đến mới todo list!")
    add_task("học bài Git va Github")
    add_task("Làm bài tập thực hành ở nhà")
 