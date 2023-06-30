// note: to handle errors where you don't want a markdown file in the sidebar, add it as a comment.
// this will fix errors like `Error: File not accounted for in sidebar: ...`
module.exports = {
  // users
  // architects
  // modelers
  // developers
  // operators

  overviewSidebar: [
    {
      label: "Getting Started",
      type: "category",
      collapsed: true,
      items: [
        // By the end of this section, readers should understand the core use cases that DataHub addresses,
        // target end-users, high-level architecture, & hosting options
        {
          type: "doc",
          label: "Introduction",
          id: "docs/features",
        },
        {
          type: "doc",
          label: "Quickstart",
          id: "docs/quickstart",
        },
        {
          type: "link",
          label: "Demo",
          href: "https://demo.datahubproject.io/",
        },
        "docs/what-is-datahub/datahub-concepts",
        "docs/saas",
      ],
    },
    {
      Integrations: [
        // The purpose of this section is to provide a deeper understanding of how ingestion works.
        // Readers should be able to find details for ingesting from all systems, apply transformers, understand sinks,
        // and understand key concepts of the Ingestion Framework (Sources, Sinks, Transformers, and Recipes)
        {
          type: "doc",
          label: "Introduction",
          id: "metadata-ingestion/README",
        },
        {
          "Quickstart Guides": [
            {
              BigQuery: [
                "docs/quick-ingestion-guides/bigquery/overview",
                "docs/quick-ingestion-guides/bigquery/setup",
                "docs/quick-ingestion-guides/bigquery/configuration",
              ],
            },
            {
              Redshift: [
                "docs/quick-ingestion-guides/redshift/overview",
                "docs/quick-ingestion-guides/redshift/setup",
                "docs/quick-ingestion-guides/redshift/configuration",
              ],
            },
            {
              Snowflake: [
                "docs/quick-ingestion-guides/snowflake/overview",
                "docs/quick-ingestion-guides/snowflake/setup",
                "docs/quick-ingestion-guides/snowflake/configuration",
              ],
            },
            {
              Tableau: [
                "docs/quick-ingestion-guides/tableau/overview",
                "docs/quick-ingestion-guides/tableau/setup",
                "docs/quick-ingestion-guides/tableau/configuration",
              ],
            },
            {
              PowerBI: [
                "docs/quick-ingestion-guides/powerbi/overview",
                "docs/quick-ingestion-guides/powerbi/setup",
                "docs/quick-ingestion-guides/powerbi/configuration",
              ],
            },
          ],
        },
        {
          Sources: [
            // collapse these; add push-based at top
            {
              type: "doc",
              id: "docs/lineage/airflow",
              label: "Airflow",
            },

            //"docker/airflow/local_airflow",
            "metadata-integration/java/spark-lineage/README",
            "metadata-ingestion/integration_docs/great-expectations",
            "metadata-integration/java/datahub-protobuf/README",
            //"metadata-ingestion/source-docs-template",
            {
              type: "autogenerated",
              dirName: "docs/generated/ingestion/sources", // '.' means the current docs folder
            },
          ],
        },
        {
          Sinks: [
            {
              type: "autogenerated",
              dirName: "metadata-ingestion/sink_docs",
            },
          ],
        },
        {
          Transformers: [
            "metadata-ingestion/docs/transformer/intro",
            "metadata-ingestion/docs/transformer/dataset_transformer",
          ],
        },
        {
          "Advanced Guides": [
            {
              "Scheduling Ingestion": [
                "metadata-ingestion/schedule_docs/intro",
                "metadata-ingestion/schedule_docs/cron",
                "metadata-ingestion/schedule_docs/airflow",
                "metadata-ingestion/schedule_docs/kubernetes",
              ],
            },

            "docs/platform-instances",
            "metadata-ingestion/docs/dev_guides/stateful",
            "metadata-ingestion/docs/dev_guides/classification",
            "metadata-ingestion/docs/dev_guides/add_stateful_ingestion_to_source",
            "metadata-ingestion/docs/dev_guides/sql_profiles",
          ],
        },
      ],
    },
    {
      Deployment: [
        // The purpose of this section is to provide the minimum steps required to deploy DataHub to the vendor of your choosing
        "docs/deploy/aws",
        "docs/deploy/gcp",
        "docker/README",
        "docs/deploy/kubernetes",
        "docs/deploy/environment-vars",
        {
          Authentication: [
            "docs/authentication/README",
            "docs/authentication/concepts",
            "docs/authentication/changing-default-credentials",
            "docs/authentication/guides/add-users",
            {
              "Frontend Authentication": [
                "docs/authentication/guides/jaas",
                {
                  "OIDC Authentication": [
                    "docs/authentication/guides/sso/configure-oidc-react",
                    "docs/authentication/guides/sso/configure-oidc-react-google",
                    "docs/authentication/guides/sso/configure-oidc-react-okta",
                    "docs/authentication/guides/sso/configure-oidc-react-azure",
                  ],
                },
              ],
            },
            "docs/authentication/introducing-metadata-service-authentication",
            "docs/authentication/personal-access-tokens",
          ],
        },
        {
          Authorization: [
            "docs/authorization/README",
            "docs/authorization/roles",
            "docs/authorization/policies",
            "docs/authorization/groups",
          ],
        },
        {
          "Advanced Guides": [
            "docs/how/delete-metadata",
            "docs/how/configuring-authorization-with-apache-ranger",
            "docs/how/backup-datahub",
            "docs/how/restore-indices",
            "docs/advanced/db-retention",
            "docs/advanced/monitoring",
            "docs/how/extract-container-logs",
            "docs/deploy/telemetry",
            "docs/how/kafka-config",
            "docs/deploy/confluent-cloud",
            "docs/advanced/no-code-upgrade",
            "docs/how/jattach-guide",
          ],
        },
        "docs/how/updating-datahub",
      ],
    },
    {
      API: [
        "docs/api/datahub-apis",
        {
          "GraphQL API": [
            {
              label: "Overview",
              type: "doc",
              id: "docs/api/graphql/overview",
            },
            {
              Reference: [
                {
                  type: "doc",
                  label: "Queries",
                  id: "graphql/queries",
                },
                {
                  type: "doc",
                  label: "Mutations",
                  id: "graphql/mutations",
                },
                {
                  type: "doc",
                  label: "Objects",
                  id: "graphql/objects",
                },
                {
                  type: "doc",
                  label: "Inputs",
                  id: "graphql/inputObjects",
                },
                {
                  type: "doc",
                  label: "Interfaces",
                  id: "graphql/interfaces",
                },
                {
                  type: "doc",
                  label: "Unions",
                  id: "graphql/unions",
                },
                {
                  type: "doc",
                  label: "Enums",
                  id: "graphql/enums",
                },
                {
                  type: "doc",
                  label: "Scalars",
                  id: "graphql/scalars",
                },
              ],
            },
            {
              Guides: [
                {
                  type: "doc",
                  label: "How To Set Up GraphQL",
                  id: "docs/api/graphql/how-to-set-up-graphql",
                },
                {
                  type: "doc",
                  label: "Getting Started With GraphQL",
                  id: "docs/api/graphql/getting-started",
                },
                {
                  type: "doc",
                  label: "Access Token Management",
                  id: "docs/api/graphql/token-management",
                },
              ],
            },
          ],
        },
        {
          type: "doc",
          label: "OpenAPI",
          id: "docs/api/openapi/openapi-usage-guide",
        },
        "docs/dev-guides/timeline",
        {
          "Rest.li API": [
            {
              type: "doc",
              label: "Rest.li API Guide",
              id: "docs/api/restli/restli-overview",
            },
            {
              type: "doc",
              label: "Restore Indices",
              id: "docs/api/restli/restore-indices",
            },
            {
              type: "doc",
              label: "Get Index Sizes",
              id: "docs/api/restli/get-index-sizes",
            },
            {
              type: "doc",
              label: "Truncate Timeseries Aspect",
              id: "docs/api/restli/truncate-time-series-aspect",
            },
            {
              type: "doc",
              label: "Evaluate Tests",
              id: "docs/api/restli/evaluate-tests",
            },
            {
              type: "doc",
              label: "Aspect Versioning and Rest.li Modeling",
              id: "docs/advanced/aspect-versioning",
            },
          ],
        },
        {
          "Python SDK": [
            "metadata-ingestion/as-a-library",
            {
              "Python SDK Reference": [
                {
                  type: "autogenerated",
                  dirName: "python-sdk",
                },
              ],
            },
          ],
        },
        "metadata-integration/java/as-a-library",
        {
          "API and SDK Guides": [
            "docs/advanced/patch",
            "docs/api/tutorials/datasets",
            "docs/api/tutorials/lineage",
            "docs/api/tutorials/tags",
            "docs/api/tutorials/terms",
            "docs/api/tutorials/owners",
            "docs/api/tutorials/domains",
            "docs/api/tutorials/deprecation",
            "docs/api/tutorials/descriptions",
            "docs/api/tutorials/custom-properties",
            "docs/api/tutorials/ml",
          ],
        },
        {
          type: "category",
          label: "DataHub CLI",
          link: { type: "doc", id: "docs/cli" },
          items: ["docs/datahub_lite"],
        },
        {
          type: "category",
          label: "Datahub Actions",
          link: { type: "doc", id: "docs/act-on-metadata" },
          items: [
            "docs/actions/README",
            "docs/actions/quickstart",
            "docs/actions/concepts",
            {
              Sources: [
                {
                  type: "autogenerated",
                  dirName: "docs/actions/sources",
                },
              ],
            },
            {
              Events: [
                {
                  type: "autogenerated",
                  dirName: "docs/actions/events",
                },
              ],
            },
            {
              Actions: [
                {
                  type: "autogenerated",
                  dirName: "docs/actions/actions",
                },
              ],
            },
            {
              Guides: [
                {
                  type: "autogenerated",
                  dirName: "docs/actions/guides",
                },
              ],
            },
          ],
        },
      ],
    },
    {
      Features: [
        "docs/ui-ingestion",
        "docs/how/search",
        "docs/schema-history",
        // "docs/how/ui-tabs-guide",
        "docs/domains",
        "docs/dataproducts",
        "docs/glossary/business-glossary",
        "docs/tags",
        "docs/ownership/ownership-types",
        "docs/browse",
        "docs/authorization/access-policies-guide",
        "docs/features/dataset-usage-and-query-history",
        "docs/posts",
        "docs/sync-status",
        "docs/architecture/stemming_and_synonyms",
        "docs/lineage/lineage-feature-guide",
        {
          type: "doc",
          id: "docs/tests/metadata-tests",
          className: "saasOnly",
        },
        "docs/act-on-metadata/impact-analysis",
      ],
    },
    {
      Develop: [
        // The purpose of this section is to provide developers & technical users with
        // concrete tutorials for how to work with the DataHub CLI & APIs
        {
          "DataHub Metadata Model": [
            "docs/modeling/metadata-model",
            "docs/modeling/extending-the-metadata-model",
            "docs/what/mxe",
            {
              Entities: [
                {
                  type: "autogenerated",
                  dirName: "docs/generated/metamodel/entities", // '.' means the current docs folder
                },
              ],
            },
          ],
        },
        {
          Architecture: [
            "docs/architecture/architecture",
            "docs/components",
            "docs/architecture/metadata-ingestion",
            "docs/architecture/metadata-serving",
          ],
        },
        {
          "Developing on DataHub": [
            "docs/developers",
            "docs/docker/development",
            "metadata-ingestion/developing",
            "docs/api/graphql/graphql-endpoint-development",
            {
              Modules: [
                "datahub-web-react/README",
                "datahub-frontend/README",
                "datahub-graphql-core/README",
                "metadata-service/README",
                "metadata-jobs/mae-consumer-job/README",
                "metadata-jobs/mce-consumer-job/README",
              ],
            },
          ],
        },
        "docs/plugins",
        {
          Troubleshooting: [
            "docs/troubleshooting/quickstart",
            "docs/troubleshooting/build",
            "docs/troubleshooting/general",
          ],
        },
        {
          Advanced: [
            "metadata-ingestion/docs/dev_guides/reporting_telemetry",
            "docs/advanced/mcp-mcl",
            "docker/datahub-upgrade/README",
            "docs/advanced/no-code-modeling",
            "datahub-web-react/src/app/analytics/README",
            "docs/how/migrating-graph-service-implementation",
            "docs/advanced/field-path-spec-v2",
            "metadata-ingestion/adding-source",
            "docs/how/add-custom-ingestion-source",
            "docs/how/add-custom-data-platform",
            "docs/advanced/browse-paths-upgrade",
          ],
        },
      ],
    },
    {
      Community: [
        "docs/slack",
        "docs/townhalls",
        "docs/townhall-history",
        "docs/CODE_OF_CONDUCT",
        "docs/CONTRIBUTING",
        "docs/links",
        "docs/rfc",
      ],
    },
    {
      "Managed DataHub": [
        "docs/managed-datahub/managed-datahub-overview",
        "docs/managed-datahub/welcome-acryl",
        {
          type: "doc",
          id: "docs/managed-datahub/saas-slack-setup",
          className: "saasOnly",
        },
        {
          type: "doc",
          id: "docs/managed-datahub/approval-workflows",
          className: "saasOnly",
        },
        {
          "Metadata Ingestion With Acryl": [
            "docs/managed-datahub/metadata-ingestion-with-acryl/ingestion",
          ],
        },
        {
          "DataHub API": [
            {
              type: "doc",
              id: "docs/managed-datahub/datahub-api/entity-events-api",
              className: "saasOnly",
            },
            {
              "GraphQL API": [
                "docs/managed-datahub/datahub-api/graphql-api/getting-started",
                {
                  type: "doc",
                  id: "docs/managed-datahub/datahub-api/graphql-api/incidents-api-beta",
                  className: "saasOnly",
                },
              ],
            },
          ],
        },
        {
          Integrations: [
            {
              type: "doc",
              id: "docs/managed-datahub/integrations/aws-privatelink",
              className: "saasOnly",
            },
            {
              type: "doc",
              id: "docs/managed-datahub/integrations/oidc-sso-integration",
              className: "saasOnly",
            },
          ],
        },
        {
          "Operator Guide": [
            {
              type: "doc",
              id: "docs/managed-datahub/operator-guide/setting-up-remote-ingestion-executor-on-aws",
              className: "saasOnly",
            },
            {
              type: "doc",
              id: "docs/managed-datahub/operator-guide/setting-up-events-api-on-aws-eventbridge",
              className: "saasOnly",
            },
          ],
        },
        {
          type: "doc",
          id: "docs/managed-datahub/chrome-extension",
          className: "saasOnly",
        },
        {
          "Managed DataHub Release History": [
            "docs/managed-datahub/release-notes/v_0_2_9",
            "docs/managed-datahub/release-notes/v_0_2_8",
            "docs/managed-datahub/release-notes/v_0_2_7",
            "docs/managed-datahub/release-notes/v_0_2_6",
            "docs/managed-datahub/release-notes/v_0_2_5",
            "docs/managed-datahub/release-notes/v_0_2_4",
            "docs/managed-datahub/release-notes/v_0_2_3",
            "docs/managed-datahub/release-notes/v_0_2_2",
            "docs/managed-datahub/release-notes/v_0_2_1",
            "docs/managed-datahub/release-notes/v_0_2_0",
            "docs/managed-datahub/release-notes/v_0_1_73",
            "docs/managed-datahub/release-notes/v_0_1_72",
            "docs/managed-datahub/release-notes/v_0_1_70",
            "docs/managed-datahub/release-notes/v_0_1_69",
          ],
        },
      ],
    },
    {
      "Release History": ["releases"],
    },

    // "Candidates for Deprecation": [
    // "README",
    // "docs/roadmap",
    // "docs/advanced/backfilling",
    //"docs/advanced/derived-aspects",
    //"docs/advanced/entity-hierarchy",
    //"docs/advanced/partial-update",
    //"docs/advanced/pdl-best-practices",
    //"docs/introducing-metadata-service-authentication"
    //"metadata-models-custom/README"
    //"metadata-ingestion/examples/transforms/README"
    //"docs/what/graph",
    //"docs/what/search-index",
    //"docs/how/add-new-aspect",
    //"docs/how/build-metadata-service",
    //"docs/how/graph-onboarding",
    //"docs/demo/graph-onboarding",
    //"metadata-ingestion-modules/airflow-plugin/README"
    // "metadata-ingestion/schedule_docs/datahub", // we can delete this
    // TODO: change the titles of these, removing the "What is..." portion from the sidebar"
    // "docs/what/entity",
    // "docs/what/aspect",
    // "docs/what/urn",
    // "docs/what/relationship",
    // "docs/advanced/high-cardinality",
    // "docs/what/search-document",
    // "docs/what/snapshot",
    // "docs/what/delta",
    // - "docker/datahub-frontend/README",
    // - "docker/datahub-gms/README",
    // - "docker/datahub-mae-consumer/README",
    // - "docker/datahub-mce-consumer/README",
    // - "docker/datahub-ingestion/README",
    // - "docker/elasticsearch-setup/README",
    // - "docker/ingestion/README",
    // - "docker/kafka-setup/README",
    // - "docker/mariadb/README",
    // - "docker/mysql/README",
    // - "docker/neo4j/README",
    // - "docker/postgres/README",
    // - "perf-test/README",
    // "metadata-jobs/README",
    // "docs/how/add-user-data",
    // "docs/_feature-guide-template"
    // ],
  ],
};