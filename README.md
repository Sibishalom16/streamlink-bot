# StreamLink 🚀

> A Telegram-based large-file delivery system that generates temporary download links with resumable HTTP streaming support.

## 📌 Overview

**StreamLink** is a learning-focused file delivery system built around Telegram, designed to convert uploaded files into secure, temporary download links.

Users can send an authorized file to the StreamLink Telegram bot and receive a unique download URL. The generated URL can be opened in a browser or used with download managers that support HTTP downloads and range-based resuming.

The project is being built as a multi-service system to explore real-world backend architecture, large-file streaming, caching, temporary links, database design, and containerized deployment.

---

## ✨ Planned Features

- 🤖 Telegram bot for file submission
- 🔗 Secure temporary download links
- ⏰ Automatic link expiration
- 📦 Large-file support
- ⚡ HTTP streaming
- 🔄 Resumable downloads using HTTP Range Requests
- 📊 Download tracking
- 👥 User management
- ⚡ Redis-based TTL and caching
- 💾 Configurable file cache
- 🧹 Automatic cache cleanup
- 🔐 Secure token-based file access
- 🐳 Docker-based development and deployment
- 🌐 Web-based download page
- 👑 Admin management features

---

## 🏗️ Architecture

```text
                         ┌──────────────┐
                         │    USER      │
                         └──────┬───────┘
                                │
                       Upload / Download
                                │
                ┌───────────────┴───────────────┐
                │                               │
                ▼                               ▼
        ┌──────────────┐                ┌──────────────┐
        │ Telegram Bot │                │   Next.js    │
        │    Python    │                │   Web UI     │
        └──────┬───────┘                └──────┬───────┘
               │                               │
               └──────────────┬────────────────┘
                              ▼
                       ┌─────────────┐
                       │ PostgreSQL  │
                       │  Metadata   │
                       └──────┬──────┘
                              │
                       ┌──────▼──────┐
                       │    Redis    │
                       │ TTL / Cache │
                       └──────┬──────┘
                              │
                              ▼
                     ┌────────────────┐
                     │  Go Download   │
                     │    Server      │
                     └───────┬────────┘
                             │
                    HTTP Streaming
                    + Range Requests
                             │
                    ┌────────┴────────┐
                    ▼                 ▼
                 Chrome              FDM
```

---

## 🛠️ Tech Stack

### Telegram Layer
- Python
- Telegram client/bot library

### Backend
- Go
- HTTP Streaming
- HTTP Range Requests

### Frontend
- Next.js
- TypeScript

### Database
- PostgreSQL

### Cache
- Redis

### Infrastructure
- Docker
- Nginx

### Version Control
- Git
- GitHub

---

## 📂 Project Structure

The project will be organized as a multi-service application:

```text
streamlink-bot/
│
├── bot/
│   └── Telegram service
│
├── server/
│   └── Go download/streaming service
│
├── web/
│   └── Next.js download interface
│
├── database/
│   └── Database schema and migrations
│
├── docker/
│   └── Container configuration
│
├── docs/
│   └── Architecture and project documentation
│
├── .env.example
├── .gitignore
├── docker-compose.yml
└── README.md
```

---

## 🔄 Basic Flow

```text
User
  │
  │ Sends authorized file
  ▼
StreamLink Telegram Bot
  │
  │ Extract metadata
  ▼
PostgreSQL
  │
  │ Generate secure token
  ▼
Temporary Download URL
  │
  ▼
Next.js Download Page
  │
  │ Download
  ▼
Go Streaming Server
  │
  │ HTTP Stream + Range Support
  ▼
Browser / Free Download Manager
```

---

## 🔗 Temporary Links

Each uploaded file receives a unique download token.

Example:

```text
https://yourdomain.com/d/a8Kx92Lm
```

A link can have an expiration period such as:

```text
1 hour
6 hours
24 hours
3 days
7 days
```

Multiple downloads can be allowed while the link remains active.

After expiration:

```text
❌ Download link expired
```

---

## 💾 Database Design

PostgreSQL stores file and system metadata rather than large file contents.

### Users

```text
id
telegram_user_id
username
created_at
```

### Files

```text
id
filename
size
mime_type
telegram_reference
status
created_at
```

### Download Links

```text
id
file_id
token
expires_at
download_count
created_at
status
```

### Download Logs

```text
id
file_id
user_id
started_at
completed_at
bytes_sent
status
```

---

## ⚡ Redis

Redis will be used for fast temporary operations such as:

- Link expiration
- Token lookup
- Rate limiting
- Download sessions
- Cache metadata

Example concept:

```text
token:a8Kx92Lm
TTL: 86400
```

After the TTL expires, the temporary key is automatically removed.

---

## 🔄 Resumable Downloads

StreamLink is designed to support HTTP Range Requests.

Example:

```http
Range: bytes=2500000000-
```

The server can respond with:

```http
206 Partial Content
```

This allows supported download managers to resume interrupted downloads.

Example:

```text
5 GB file
     ↓
2.5 GB downloaded
     ↓
Connection interrupted
     ↓
Resume
     ↓
Continue from 2.5 GB
```

---

## 💾 Cache Strategy

A configurable cache will be introduced in a later development phase.

Target example:

```text
CACHE_LIMIT = 100 GB
```

When the cache reaches the configured limit, StreamLink can remove older or least-recently-used eligible files to maintain available storage.

The cache system will be implemented after the core download pipeline is stable.

---

## 🔐 Security

StreamLink will follow basic security practices:

- Random, unpredictable download tokens
- Expiring links
- Environment-based secrets
- Input validation
- Rate limiting
- Protected Telegram credentials
- No large files stored directly in PostgreSQL
- Controlled file access
- Secure production configuration

---

## 🧪 Development Roadmap

### Phase 0 — Planning & Architecture
- [x] Project concept
- [x] Tech stack
- [x] Architecture
- [x] Database concept
- [x] Security model
- [ ] Repository initialization

### Phase 1 — Telegram Bot
- [ ] `/start`
- [ ] `/help`
- [ ] `/about`
- [ ] `/ping`
- [ ] Basic bot configuration

### Phase 2 — File Receiving
- [ ] Detect uploaded files
- [ ] Extract metadata
- [ ] Handle supported file types
- [ ] Store file metadata

### Phase 3 — PostgreSQL
- [ ] Database setup
- [ ] Users table
- [ ] Files table
- [ ] Download links table
- [ ] Download logs table

### Phase 4 — Link Generator
- [ ] Secure token generation
- [ ] Download URL generation
- [ ] Bot response

### Phase 5 — Redis
- [ ] Redis integration
- [ ] TTL
- [ ] Link expiration
- [ ] Rate limiting

### Phase 6 — Web Interface
- [ ] Next.js setup
- [ ] Download page
- [ ] File information
- [ ] Expiration status
- [ ] Download button

### Phase 7 — Go Streaming Server
- [ ] Go HTTP server
- [ ] Streaming
- [ ] Content headers
- [ ] Large-file handling

### Phase 8 — File Retrieval
- [ ] Telegram file retrieval layer
- [ ] Streaming integration
- [ ] Large-file testing

### Phase 9 — Resumable Downloads
- [ ] HTTP Range Requests
- [ ] Partial Content
- [ ] FDM testing
- [ ] Resume support

### Phase 10 — Analytics
- [ ] Download count
- [ ] Download logs
- [ ] Statistics

### Phase 11 — Cache
- [ ] Cache layer
- [ ] 100 GB configurable limit
- [ ] LRU cleanup
- [ ] Cache monitoring

### Phase 12 — Security
- [ ] Rate limiting
- [ ] Access validation
- [ ] Abuse protection
- [ ] Security hardening

### Phase 13 — Admin
- [ ] Admin commands
- [ ] User statistics
- [ ] File statistics
- [ ] Download statistics

### Phase 14 — Docker
- [ ] Dockerfiles
- [ ] Docker Compose
- [ ] Service networking
- [ ] Local production-like environment

### Phase 15 — Testing
- [ ] Unit tests
- [ ] Integration tests
- [ ] Large-file tests
- [ ] Resume tests
- [ ] Concurrent download tests

### Phase 16 — Deployment
- [ ] Server setup
- [ ] Nginx
- [ ] HTTPS
- [ ] Production deployment
- [ ] Monitoring

### Phase 17 — Documentation
- [ ] Setup guide
- [ ] Architecture documentation
- [ ] API documentation
- [ ] Deployment guide
- [ ] Troubleshooting guide

---

## ⚠️ Usage

StreamLink should be used only for files that the user has the legal right or authorization to distribute.

The project is intended primarily as a learning and engineering project focused on file delivery, streaming, distributed services, and backend architecture.

---

## 🎯 Project Goals

The main goal of StreamLink is to gain practical experience with:

- Distributed backend architecture
- Telegram APIs
- Python
- Go
- PostgreSQL
- Redis
- HTTP streaming
- Range Requests
- Caching
- Authentication
- Docker
- Reverse proxies
- Cloud deployment
- Large-file delivery

---

## 👨‍💻 Author

**Sibi Raj**

Computer Science Engineering Student  
Chennai, India

---

## 📜 License

License information will be added as the project develops.
