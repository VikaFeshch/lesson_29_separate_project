# Build and check the image
```bash
docker build -t lesson_29-project:latest -f Dockerfile.demo .
docker build -t lesson_29-chrome:latest -f Dockerfile.chrome .
docker build -t lesson_29-hw29:latest -f Dockerfile.hw29 .
```

# Run the container in interactive mode
```bash
docker run --rm -it lesson_29-project:latest bash
docker run --rm -it lesson_29-hw29:latest bash
```

```
# Run locally with report creation
pytest --html=local_reports/report.html
```
