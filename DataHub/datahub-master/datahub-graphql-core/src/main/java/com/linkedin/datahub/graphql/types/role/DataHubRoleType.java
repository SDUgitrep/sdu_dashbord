package com.linkedin.datahub.graphql.types.role;

import com.google.common.collect.ImmutableSet;
import com.linkedin.common.urn.Urn;
import com.linkedin.datahub.graphql.QueryContext;
import com.linkedin.datahub.graphql.generated.DataHubRole;
import com.linkedin.datahub.graphql.generated.Entity;
import com.linkedin.datahub.graphql.generated.EntityType;
import com.linkedin.datahub.graphql.types.role.mappers.DataHubRoleMapper;
import com.linkedin.entity.EntityResponse;
import com.linkedin.entity.client.EntityClient;
import graphql.execution.DataFetcherResult;
import java.net.URISyntaxException;
import java.util.ArrayList;
import java.util.HashSet;
import java.util.List;
import java.util.Map;
import java.util.Set;
import java.util.function.Function;
import java.util.stream.Collectors;
import javax.annotation.Nonnull;
import lombok.RequiredArgsConstructor;

import static com.linkedin.metadata.Constants.*;


@RequiredArgsConstructor
public class DataHubRoleType implements com.linkedin.datahub.graphql.types.EntityType<DataHubRole, String> {
  static final Set<String> ASPECTS_TO_FETCH = ImmutableSet.of(DATAHUB_ROLE_INFO_ASPECT_NAME);
  private final EntityClient _entityClient;

  @Override
  public EntityType type() {
    return EntityType.DATAHUB_ROLE;
  }

  @Override
  public Function<Entity, String> getKeyProvider() {
    return Entity::getUrn;
  }

  @Override
  public Class<DataHubRole> objectClass() {
    return DataHubRole.class;
  }

  @Override
  public List<DataFetcherResult<DataHubRole>> batchLoad(@Nonnull List<String> urns, @Nonnull QueryContext context)
      throws Exception {
    final List<Urn> roleUrns = urns.stream().map(this::getUrn).collect(Collectors.toList());

    try {
      final Map<Urn, EntityResponse> entities =
          _entityClient.batchGetV2(DATAHUB_ROLE_ENTITY_NAME, new HashSet<>(roleUrns), ASPECTS_TO_FETCH,
              context.getAuthentication());

      final List<EntityResponse> gmsResults = new ArrayList<>();
      for (Urn urn : roleUrns) {
        gmsResults.add(entities.getOrDefault(urn, null));
      }
      return gmsResults.stream()
          .map(gmsResult -> gmsResult == null ? null
              : DataFetcherResult.<DataHubRole>newResult().data(DataHubRoleMapper.map(gmsResult)).build())
          .collect(Collectors.toList());
    } catch (Exception e) {
      throw new RuntimeException("Failed to batch load Roles", e);
    }
  }

  private Urn getUrn(final String urnStr) {
    try {
      return Urn.createFromString(urnStr);
    } catch (URISyntaxException e) {
      throw new RuntimeException(String.format("Failed to convert urn string %s into Urn", urnStr));
    }
  }
}
