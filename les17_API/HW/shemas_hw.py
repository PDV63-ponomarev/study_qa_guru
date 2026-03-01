get_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "data": {
      "type": "object",
      "properties": {
        "id": {
          "type": "integer"
        },
        "email": {
          "type": "string"
        },
        "first_name": {
          "type": "string"
        },
        "last_name": {
          "type": "string"
        },
        "avatar": {
          "type": "string"
        }
      },
      "required": [
        "id",
        "email",
        "first_name",
        "last_name",
        "avatar"
      ]
    },
    "support": {
      "type": "object",
      "properties": {
        "url": {
          "type": "string"
        },
        "text": {
          "type": "string"
        }
      },
      "required": [
        "url",
        "text"
      ]
    },
    "_meta": {
      "type": "object",
      "properties": {
        "powered_by": {
          "type": "string"
        },
        "docs_url": {
          "type": "string"
        },
        "upgrade_url": {
          "type": "string"
        },
        "example_url": {
          "type": "string"
        },
        "variant": {
          "type": "string"
        },
        "message": {
          "type": "string"
        },
        "cta": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "label",
            "url"
          ]
        },
        "context": {
          "type": "string"
        }
      },
      "required": [
        "powered_by",
        "docs_url",
        "upgrade_url",
        "example_url",
        "variant",
        "message",
        "cta",
        "context"
      ]
    }
  },
  "required": [
    "data",
    "support",
    "_meta"
  ]
}

post_user = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "id": {
      "type": "string"
    },
    "createdAt": {
      "type": "string"
    },
    "_meta": {
      "type": "object",
      "properties": {
        "powered_by": {
          "type": "string"
        },
        "docs_url": {
          "type": "string"
        },
        "upgrade_url": {
          "type": "string"
        },
        "example_url": {
          "type": "string"
        },
        "variant": {
          "type": "string"
        },
        "message": {
          "type": "string"
        },
        "cta": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "label",
            "url"
          ]
        },
        "context": {
          "type": "string"
        }
      },
      "required": [
        "powered_by",
        "docs_url",
        "upgrade_url",
        "example_url",
        "variant",
        "message",
        "cta",
        "context"
      ]
    }
  },
  "required": [
    "id",
    "createdAt",
    "_meta"
  ]
}

put_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "updatedAt": {
      "type": "string"
    },
    "_meta": {
      "type": "object",
      "properties": {
        "powered_by": {
          "type": "string"
        },
        "docs_url": {
          "type": "string"
        },
        "upgrade_url": {
          "type": "string"
        },
        "example_url": {
          "type": "string"
        },
        "variant": {
          "type": "string"
        },
        "message": {
          "type": "string"
        },
        "cta": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "label",
            "url"
          ]
        },
        "context": {
          "type": "string"
        }
      },
      "required": [
        "powered_by",
        "docs_url",
        "upgrade_url",
        "example_url",
        "variant",
        "message",
        "cta",
        "context"
      ]
    }
  },
  "required": [
    "updatedAt",
    "_meta"
  ]
}

patch_users = {
  "$schema": "http://json-schema.org/draft-04/schema#",
  "type": "object",
  "properties": {
    "updatedAt": {
      "type": "string"
    },
    "_meta": {
      "type": "object",
      "properties": {
        "powered_by": {
          "type": "string"
        },
        "docs_url": {
          "type": "string"
        },
        "upgrade_url": {
          "type": "string"
        },
        "example_url": {
          "type": "string"
        },
        "variant": {
          "type": "string"
        },
        "message": {
          "type": "string"
        },
        "cta": {
          "type": "object",
          "properties": {
            "label": {
              "type": "string"
            },
            "url": {
              "type": "string"
            }
          },
          "required": [
            "label",
            "url"
          ]
        },
        "context": {
          "type": "string"
        }
      },
      "required": [
        "powered_by",
        "docs_url",
        "upgrade_url",
        "example_url",
        "variant",
        "message",
        "cta",
        "context"
      ]
    }
  },
  "required": [
    "updatedAt",
    "_meta"
  ]
}

new_shemas = {
    "$schema": "http://json-schema.org/draft-04/schema#",
    "type": "object",
    "properties": {
        "name": {"type": "string"},  # опционально
        "job": {"type": "string"},   # опционально
        "id": {"type": "string"},
        "createdAt": {"type": "string"},
        "_meta": {"type": "object"}
    },
    # Не делаем name и job обязательными
    "required": ["id", "createdAt"]
}