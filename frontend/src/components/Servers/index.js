import React from 'react';
import Server from '../Server';
import css from './Servers.css';


import {
  QueryRenderer,
  graphql,
} from 'react-relay';
import {
  Environment,
  Network,
  RecordSource,
  Store,
} from 'relay-runtime';

function fetchQuery(
  operation,
  variables,
) {
  return fetch('/graphql', {
    method: 'POST',
    headers: {
      'Content-Type': 'application/json',
    },
    body: JSON.stringify({
      query: operation.text,
      variables,
    }),
  }).then(response => {
    return response.json();
  });
}

const modernEnvironment = new Environment({
  network: Network.create(fetchQuery),
  store: new Store(new RecordSource()),
});

const Servers = () => (
  <div className={css.component}>
    <QueryRenderer
      environment={modernEnvironment}
      query={graphql`
        query ServersQuery {
          allServers {
            edges {
              node {
                name,
                ip,
                id,
              }
            }
          }
        }
      `}
      variables={{}}
      render={({error, props}) => {
        if (props) {
          console.log(props);
          return (
            <div className={css.servers}>
              {props.allServers.edges.map(edge => (
                <Server key={edge.node.id} name={edge.node.name} ip={edge.node.ip} />
              ))}
            </div>
          );
        } else {
          return <div>'Loading'</div>;
        }
      }}
    />
  </div>
);

export default Servers;
