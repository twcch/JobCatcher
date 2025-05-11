# 104 Job Crawler

A Python-based web crawler for Taiwan's 104 job board (104.com.tw). This project follows enterprise-level design patterns and SOLID principles, featuring modular architecture, comprehensive error handling, and logging capabilities.

## Features

- Multi-criteria job search:
  - Keywords
  - Location (e.g., 6001001000 for Taipei City)
  - Job category (e.g., 2001001000 for Software Engineer)
  - Salary range
  - Work experience
  - Education requirements
- Comprehensive error handling
- Detailed logging system
- Modular design for easy extension
- CSV export functionality
- Type hints and dataclass usage
- Clean architecture with separation of concerns

## Project Structure

```
.
├── src/
│   ├── config/         # Configuration settings
│   │   └── settings.py # App configuration
│   ├── models/         # Data models
│   │   └── job.py     # Job data model
│   ├── repositories/   # Data access layer
│   │   └── job_repository.py # Job data access
│   ├── services/       # Business logic layer
│   │   └── job_service.py # Job-related services
│   └── utils/          # Utility functions
│       └── logger.py   # Logging configuration
├── tests/              # Test files
├── setup.py           # Package installation
├── requirements.txt   # Project dependencies
└── README.md         # Project documentation
```

## Design Patterns Used

- Repository Pattern: Abstracts data access
- Service Layer: Handles business logic
- Factory Pattern: Manages object creation
- Dependency Injection: Injects dependencies through constructors

## Installation

1. Clone the repository:
```bash
git clone [repository-url]
cd [project-directory]
```

2. Create and activate a virtual environment (recommended):
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Install the package in development mode:
```bash
pip install -e .
```

## Usage

Run the crawler:
```bash
python run.py
```

Follow the prompts to enter search criteria:
- Keywords
- Location (e.g., 6001001000 for Taipei City)
- Job category (e.g., 2001001000 for Software Engineer)
- Salary range
- Work experience
- Education requirements

The results will be saved to `jobs.csv` in the project root directory.

## Development

### Code Quality Tools

The project uses several tools to maintain code quality:
- black: Code formatting
- isort: Import sorting
- mypy: Type checking
- pytest: Unit testing

### Running Tests

```bash
pytest
```

### Code Style

The project follows PEP 8 guidelines and uses type hints throughout the codebase.

## Error Handling

The project implements comprehensive error handling:
- Network request errors
- JSON parsing errors
- File I/O errors
- Data validation errors

## Logging

Logs are written to both:
- Console output
- `job_crawler.log` file

Log levels can be configured in `src/config/settings.py`.

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License

## Author

[Your Name]

## Acknowledgments

- 104.com.tw for providing the job board
- Python community for the excellent tools and libraries 