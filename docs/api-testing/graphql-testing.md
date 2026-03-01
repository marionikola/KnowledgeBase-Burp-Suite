# GraphQL Testing - Burp Suite

## Apa itu GraphQL?

GraphQL adalah query language untuk APIs yang memungkinkan client untuk meminta data yang dibutuhkan.

## GraphQL Basics

### Query (Read)
```graphql
query {
  user(id: "1") {
    name
    email
  }
}
```

### Mutation (Write)
```graphql
mutation {
  createUser(name: "test") {
    id
    name
  }
}
```

### Introspection
```graphql
query {
  __schema {
    types {
      name
    }
  }
}
```

## Vulnerabilities

### 1. IDOR in GraphQL
```graphql
query {
  user(id: "1") {
    # Test accessing other users
  }
}
```

### 2. Batching Attacks
```graphql
query {
  user1: user(id: "1") { password }
  user2: user(id: "2") { password }
}
```

### 3. Introspection Enabled
```graphql
query {
  __schema {
    # Exposes entire API!
  }
}
```

### 4. SQL Injection
```graphql
query {
  user(name: "' OR '1'='1") {
    id
  }
}
```

## Testing dengan Burp

### Enable in Proxy
```
# Proxy > Options > HTTP Protocol
# Enable WebSocket and SPDY support
```

### Introspection
```
# Find:
POST /graphql
or
POST /api/graphql

# Send:
{"query": "{__schema{types{name}}}"}
```

### Discovery
```
# Common endpoints:
/graphql
/graphql/console
/api
/graphiql
/v1/graphql
```

## Tools

### Repeater
```
- Test queries
- Modify mutations
- Analyze responses
```

### Intruder
```
- Batch attacks
- Fuzz parameters
- Enumerate IDs
```

### Extensions
```
- GraphQL Batcher
- Altair GraphQL Client
```

---

**Version**: 1.0.7-20260301-Minggu-1011-WIB  
**Author**: waktuberhenti
