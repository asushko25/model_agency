### Testing application using Locust.
- We can test application using Locust, which allows to mimic real user traffic, finding bottlenecks, testing
  performance of our application.
  - Run Locust tests using Docker `docker-compose -f locust_tests/docker-compose.yml up --build -d`
    - Creates 1 Master and 1 Worker - which executes tests.
    - We can make more Workers by using `--scale worker=4` in 
      `docker-compose -f locust_tests/docker-compose.yml up --build --scale worker=4 -d`
    - Each worker is a separate process. If you have 4 CPUs and run 10 workers, they may compete for resources,
      which can affect performance. Usually, 1-2 workers per CPU core is recommended, but it depends on the type of test.
  - After Docker Locust is running you can enter `http://localhost:8089/` if testing locally.
  - To stop Docker containers use `docker-compose -f locust_tests/docker-compose.yml down`
