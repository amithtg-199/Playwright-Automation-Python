import logging
from datetime import datetime
from pathlib import Path


class DailyFileHandler(logging.Handler):

    def __init__(self, log_dir="loggers/logs", retention_days=7):
        super().__init__()

        self.log_dir = Path(log_dir)
        self.log_dir.mkdir(parents=True, exist_ok=True)

        self.retention_days = retention_days
        self.current_date = None
        self.file_handler = None

        self._open_log_file()
        self._cleanup_old_logs()

    def _get_log_file(self):
        date_string = datetime.now().strftime("%Y-%m-%d")
        return self.log_dir / f"pytest_{date_string}.log"

    def _open_log_file(self):
        today = datetime.now().date()

        if self.current_date == today:
            return

        self.current_date = today

        if self.file_handler:
            self.file_handler.close()

        self.file_handler = logging.FileHandler(
            self._get_log_file(),
            mode="a",
            encoding="utf-8"
        )

        formatter = logging.Formatter(
            "%(asctime)s | %(levelname)-8s | %(name)s | %(message)s",
            datefmt="%Y-%m-%d %H:%M:%S"
        )

        self.file_handler.setFormatter(formatter)

    def emit(self, record):
        try:
            self._open_log_file()
            self.file_handler.emit(record)
        except Exception:
            self.handleError(record)

    def _cleanup_old_logs(self):
        log_files = sorted(
            self.log_dir.glob("pytest_*.log"),
            key=lambda path: path.stat().st_mtime,
            reverse=True
        )

        for old_file in log_files[self.retention_days:]:
            try:
                old_file.unlink()
            except OSError:
                pass

    def close(self):
        if self.file_handler:
            self.file_handler.close()

        super().close()