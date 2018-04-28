# Patching the ESI client

The auto-generated EVE Swagger Interface client [described
here](https://developers.eveonline.com/blog/article/swagger-codegen)
unfortunately has some erroneous imports. I created a patch to fix these
problems. Apply as follows:

```shell
unzip /path/to/generated-client.zip
cd python-client
patch -p1 < /path/to/swagger_client.patch
```

Note that I already applied the path to the current contents of the
swagger_client directory. This is meant to document things for possible future
upgrades.
