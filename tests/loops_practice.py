import random
import time

TOTAL_ITERATIONS = 10
LOAD_THRESHOLD = 85
SLEEP_SECONDS = 0.2
MIN_LOAD = 0
MAX_LOAD = 100


def monitor_load() -> None:
    """
    Симулирует мониторинг нагрузки на систему.
    Генерирует случайные значения нагрузки, выводит предупреждение,
    если нагрузка превышает пороговое значение.
    """
    print("=== Мониторинг нагрузки запущен ===")

    for iteration in range(1, TOTAL_ITERATIONS + 1):
        # Генерируем случайную нагрузку
        current_load = random.randint(MIN_LOAD, MAX_LOAD)

        # Формируем сообщение
        status = "⚠️  ПРЕВЫШЕНИЕ!" if current_load > LOAD_THRESHOLD else "✅  Норма"

        print(f"Итерация {iteration:2d}: нагрузка {current_load:3d}%  {status}")

        # Пауза перед следующей итерацией
        time.sleep(SLEEP_SECONDS)

    print("=== Мониторинг завершён ===")


if __name__ == "__main__":
    monitor_load()
