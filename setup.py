#!/usr/bin/env python3
"""
Test setup.py file for dependency confusion detection
Contains various dependency declarations that should trigger security scanning
"""

from setuptools import setup, find_packages

# Version and metadata
__version__ = "1.2.3"

# Read requirements from file (this is a common pattern)
def read_requirements(filename):
    with open(filename, 'r') as f:
        return [line.strip() for line in f if line.strip() and not line.startswith('#')]

# Main setup configuration
setup(
    name="dependency-confusion-setup-test",
    version=__version__,
    description="Test setup.py for dependency confusion vulnerability scanning",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    author="Security Test Team",
    author_email="security-team@testcompany.com",
    url="https://github.com/testorg/dependency-confusion-setup-test",
    
    # Package discovery
    packages=find_packages(where="src", exclude=["tests*"]),
    package_dir={"": "src"},
    
    # Core runtime dependencies - mix of legitimate and suspicious
    install_requires=[
        # Legitimate packages
        "requests>=2.28.0",
        "click>=8.1.0", 
        "pyyaml>=6.0",
        "jinja2>=3.1.0",
        "cryptography>=37.0.0",
        "boto3>=1.24.0",
        
        # Suspicious internal packages (should be flagged for dependency confusion)
        "internal-auth-client==2.3.4",         # Internal authentication client
        "company-database-pool>=1.8.2",        # Database connection pooling
        "private-message-queue==3.1.7",        # Private message queue client
        "org-service-discovery>=2.4.1",        # Service discovery client
        "enterprise-config-client==1.9.5",     # Enterprise configuration client
        "custom-logging-handler>=2.2.8",       # Custom logging implementation
        "internal-metrics-publisher>=1.6.3",   # Internal metrics publishing
        "company-security-utils==4.0.1",       # Security utilities
        "private-cache-client>=2.7.4",         # Private caching client
        "org-workflow-engine==1.5.9"           # Workflow engine client
    ],
    
    # Setup-time dependencies (build requirements)
    setup_requires=[
        "setuptools>=65.0",
        "wheel>=0.37.0",
        
        # Suspicious setup dependencies (should be flagged)
        "internal-proto-compiler>=3.2.1",      # Protocol buffer compiler
        "company-code-generator==1.4.8",       # Code generation tools
        "private-asset-processor>=2.1.5",      # Asset processing tools
        "org-build-validator==1.7.2",          # Build validation tools
        "enterprise-packaging-tools>=2.8.0"    # Enterprise packaging utilities
    ],
    
    # Test dependencies
    tests_require=[
        "pytest>=7.1.0",
        "pytest-cov>=3.0.0",
        "pytest-mock>=3.8.0",
        "coverage>=6.4.0",
        
        # Suspicious test dependencies (should be flagged)
        "internal-test-fixtures>=4.1.2",       # Internal testing fixtures
        "company-mock-server==2.6.7",          # Mock server for testing
        "private-test-database>=1.9.4",        # Private test database
        "org-performance-tester==3.3.1",       # Performance testing tools
        "enterprise-integration-tests>=2.5.8"  # Integration testing framework
    ],
    
    # Extra dependencies grouped by use case
    extras_require={
        # Development environment extras
        "dev": [
            "black>=22.6.0",
            "flake8>=5.0.0", 
            "mypy>=0.971",
            "pre-commit>=2.20.0",
            
            # Suspicious dev extras (should be flagged)
            "internal-dev-server>=3.4.2",      # Internal development server
            "company-debug-toolbar==1.8.9",    # Debug toolbar
            "private-dev-proxy>=2.2.6",        # Development proxy
            "org-local-storage==1.6.4"         # Local storage emulator
        ],
        
        # Production environment extras  
        "prod": [
            "gunicorn>=20.1.0",
            "uvicorn>=0.18.0",
            "prometheus-client>=0.14.1",
            
            # Suspicious production extras (should be flagged)
            "internal-load-balancer>=5.1.3",   # Internal load balancer
            "company-monitoring-agent==3.7.2", # Monitoring agent
            "private-log-aggregator>=2.4.8",   # Log aggregation service
            "org-deployment-hooks==1.9.7",     # Deployment hooks
            "enterprise-health-checker>=4.2.1" # Health checking service
        ],
        
        # Machine learning extras
        "ml": [
            "numpy>=1.21.0",
            "pandas>=1.4.0", 
            "scikit-learn>=1.1.0",
            
            # Suspicious ML extras (should be flagged)
            "internal-model-loader>=2.8.5",    # Internal model loading
            "company-feature-engine==4.1.6",   # Feature engineering
            "private-ml-pipeline>=3.6.2",      # ML pipeline tools
            "org-experiment-tracker==2.3.9",   # Experiment tracking
            "enterprise-model-registry>=1.7.4" # Model registry client
        ],
        
        # Database extras
        "database": [
            "sqlalchemy>=1.4.0",
            "psycopg2-binary>=2.9.0",
            "redis>=4.3.0",
            
            # Suspicious database extras (should be flagged)
            "internal-db-migrator>=3.5.1",     # Database migration tools
            "company-query-optimizer==2.4.7",  # Query optimization
            "private-db-monitor>=1.8.3",       # Database monitoring
            "org-backup-scheduler==4.2.6",     # Backup scheduling
            "enterprise-db-proxy>=2.9.8"       # Database proxy
        ],
        
        # Documentation extras
        "docs": [
            "sphinx>=5.0.0",
            "sphinx-rtd-theme>=1.0.0",
            
            # Suspicious documentation extras (should be flagged)
            "internal-doc-builder>=2.1.4",     # Internal documentation builder
            "company-api-docs==1.5.8",         # API documentation generator
            "private-style-checker>=3.2.1"     # Style guide checker
        ]
    },
    
    # Python version requirement
    python_requires=">=3.8",
    
    # Package classification
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License", 
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11"
    ],
    
    # Entry points for CLI tools
    entry_points={
        "console_scripts": [
            "dep-test=dependency_test.cli:main",
            "security-scan=dependency_test.scanner:run"
        ]
    },
    
    # Package data to include
    package_data={
        "dependency_test": [
            "config/*.yaml",
            "templates/*.jinja2", 
            "static/**/*"
        ]
    },
    
    # Additional metadata
    keywords="dependency-confusion security-testing vulnerability-scanning",
    project_urls={
        "Documentation": "https://docs.testcompany.com/dependency-test",
        "Source": "https://github.com/testorg/dependency-confusion-setup-test",
        "Tracker": "https://github.com/testorg/dependency-confusion-setup-test/issues",
        
        # Potentially hijackable URLs (should trigger GitHub repo hijacking detection)
        "Legacy Docs": "https://github.com/abandoned-startup/legacy-docs",
        "Old Tools": "https://github.com/defunct-org/old-utilities",
        "Archive": "https://github.com/missing-company/project-archive"
    }
)

# Additional setup configuration that might be parsed
if __name__ == "__main__":
    # Sometimes setup.py files contain additional logic
    import sys
    
    # Example of conditional dependencies based on platform
    extra_deps = []
    if sys.platform.startswith('linux'):
        extra_deps.extend([
            "internal-linux-utils>=1.2.3",     # Linux-specific internal utilities
            "company-systemd-manager==0.9.1"   # SystemD management tools
        ])
    elif sys.platform.startswith('win'):
        extra_deps.extend([
            "internal-windows-service>=2.1.0", # Windows service utilities
            "company-registry-tools==1.4.5"    # Windows registry tools
        ])
    
    print("Setup completed successfully!")
