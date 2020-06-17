#!/usr/bin/python3

import requests
import hashlib
import socket


def md5url(url):
    r = requests.get(url, stream=True)
    md5 = hashlib.md5()
    for line in r.iter_content(5000000):
        md5.update(line)
    return md5.hexdigest()


def main():
    cdn_summary = md5url("https://dl.flathub.org/repo/summary")
    cdn_sig = md5url(f"https://dl.flathub.org/repo/summary.sig")

    master_summary = md5url("https://hub.flathub.org/repo/summary")
    master_sig = md5url(f"https://hub.flathub.org/repo/summary.sig")

    hostname = socket.gethostname()
    summary = md5url(f"https://{hostname}/repo/summary")
    sig = md5url(f"https://{hostname}/repo/summary.sig")

    summary_synced = summary == master_summary
    sig_synced = sig == master_sig
    state = int(summary_synced and sig_synced)

    cdn_summary_synced = cdn_summary == master_summary
    cdn_sig_synced = cdn_sig == master_sig
    cdn_state = int(cdn_summary_synced and cdn_sig_synced)

    output = [
        f"flathub_summary_in_sync {state}",
        f"flathub_cdn_summary_in_sync {cdn_state}",
        ""
    ]

    with open("/var/lib/node_exporter/flathub_summary.prom", "w") as f:
        f.write("\n".join(output))


if __name__ == "__main__":
    main()
