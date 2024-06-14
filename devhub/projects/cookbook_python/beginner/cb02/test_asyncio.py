import asyncio

async def task(name, seconds):
    """Async task to simulate time-consuming operations"""
    print(f'Task {name} started, will take {seconds} second(s)')
    await asyncio.sleep(seconds)
    print(f'Task {name} completed')
    return f'Result of {name}'

async def main():
    """Main function to schedule and run all tasks"""
    # create 3 task
    task1 = asyncio.create_task(task('A', 2))
    task2 = asyncio.create_task(task('B', 3))
    task3 = asyncio.create_task(task('C', 1))
    
    # wait for all tasks to complete
    results = await asyncio.gather(task1, task2, task3)
    print(f"All tasks completed. Results: {results}")

# run the main function
asyncio.run(main())
