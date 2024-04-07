# aurora-tr

Translate via aurora and variants, openai, azure openai, etc.

## url for `aurora` REST API

First off, identify `OPENAI_BASE_URL` for the `aurora` REST API to use.

To deplay your own `aurora` locolly or on a remote machine, refer to
[https://github.com/aurora-develop/aurora](https://github.com/aurora-develop/aurora)

For example (the easieast way if you can access docker):
```bash
docker run -d --name aurora -p 8080:8080 ghcr.io/aurora-develop/aurora:latest
```

The `OPENAI_BASE_URL` in this case will be `http://localhost:8080/v1` or `http://external_ip_or_domainname:8080/v1`
