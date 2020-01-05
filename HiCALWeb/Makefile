DJANGO_CMD=docker run --rm -ti \
		-e POSTGRES_HOST=localhost \
		-e DJANGO_SETTINGS_MODULE=config.settings.local \
		-v ${PWD}:/app/ \
		-v /mnt/ceph/storage/data-in-progress/kibi9872/crypsor/:/mnt/ceph/storage/data-in-progress/kibi9872/crypsor/ \
		--net=host \
		hical-django:0.0.1

docker-run-django-local:
		$(DJANGO_CMD) ./manage.py runserver

docker-set-up-db:
	echo "CREATE DATABASE hicalweb;"| psql -h localhost -U postgres &&\
	$(DJANGO_CMD) ./manage.py makemigrations &&\
	$(DJANGO_CMD) ./manage.py migrate &&\
	../../create-topics.sh

docker-run-postgres-local:
	docker run --rm -ti --net=host hical-postgres:0.0.1

docker-build-production-images:
	docker build -t hical-django:0.0.1 -f compose/local/django/Dockerfile . && \
	docker build -t hical-caddy:0.0.1 -f compose/production/caddy/Dockerfile . && \
	docker build -t hical-postgres:0.0.1 -f compose/production/postgres/Dockerfile .

