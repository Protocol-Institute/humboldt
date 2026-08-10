# Vulnerabilities, Secrets and Misconfiguration in the Highest-Exposure Docker Hub Images

**Source:** cs.CY updates on arXiv.org
**URL:** https://arxiv.org/abs/2608.02669
**Date:** 2026-08-05
**Relevance:** Directly relevant to understanding security vulnerabilities in container infrastructure, which affects the reliability and trustworthiness of widely-deployed software systems.

## Summary

arXiv:2608.02669v1 Announce Type: cross 
Abstract: Docker Hub is the registry underneath most container deployments, and a flaw in a widely reused base image is inherited by every image built on it. Prior ecosystem-scale measurements each rely on a single detector, leaving the tool-dependence of their counts unquantified, while the studies that do compare scanners use samples of tens to hundreds of images. We present ChimangoScan, a pipeline that crawls the Docker Hub namespace (12,716,568 repositories, 663.8 billion cumulative pulls), reconstructs the image layer graph (54.4 million IS_BASE_O
