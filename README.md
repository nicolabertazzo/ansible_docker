Role Name
=========

This role provides the following:

- Define a partition for Docker installation
- Installation of Docker following Docker-Engine install procedures as documented by Docker.
- Configure Docker HTTPS/TLS
- Configure Docker Swarm

Requirements
------------

This role requires Ansible 2.12 or higher.

Role Variables
--------------

| Variable                   | Required | Default        | Comments                                                     |
| -------------------------- | -------- | -------------- | ------------------------------------------------------------ |
| docker_block_device        | yes      | /dev/sdb       |                                                              |
| docker_storage_size        | yes      | 100MB          |                                                              |
| docker_version             | yes      | 20.10.14-*.el7 |                                                              |
| docker_tls_key             | yes      | None           | path to key.pem file. The file must be named as key.pem      |
| docker_tls_cert            | yes      | None           | path to cert.pem file. The file must be named as cert.pem    |
| docker_tls_ca              | yes      | None           | path to ca.pem file. The file must be named as ca.pem        |
| docker_advertise_addr      | yes      | None           | docker swarm advertise addres. https://docs.docker.com/engine/reference/commandline/swarm_init/#--advertise-addr |
| docker_remote_addrs        | No       | None           | HOST:PORT  to docker swarm                                   |
| docker_swarm_manager       | No       |                | define if the node is a manager                              |
| docker_swarm_manager_token | No       |                | Required token to join a node as manager                     |
| docker_swarm_worker        | No       |                | define if the node is a worker                               |
| docker_swarm_worker_token  | No       |                | Required token to join a node as worker                      |



License
-------

Apache-2.0

Author Information
------------------

[Nicola Bertazzo](https://github.com/nicolabertazzo)

