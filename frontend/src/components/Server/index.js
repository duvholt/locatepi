import React from 'react';
import { graphql, createFragmentContainer } from 'react-relay';
import formatRelative from 'date-fns/formatRelative';

import PropTypes from 'prop-types';
import classNames from 'classnames';
import css from './Server.css';

const Server = ({ server }) => {
  let offline = true;
  const { name, ping } = server;
  let relativeTime = null;
  if (ping) {
    relativeTime = formatRelative(new Date(ping.time), new Date());
    if (new Date() - new Date(ping.time) < 1000 * 60 * 10) {
      offline = false;
    }
  }
  return (
    <div className={css.component}>
      <div
        className={classNames(
          css.name, {
            [css.offline]: offline,
          }
        )}
      >
        { name }
      </div>
      <div className={css.content}>
        { ping && (
          <div className={css.ip}>
            <div>{ ping.ip }</div>
            <div>{ ping.localIp }</div>
          </div>
        )}
        <div className={css.date}>{relativeTime && `Last update: ${relativeTime}` }</div>
      </div>
    </div>
  );
}

Server.propTypes = {
  server: PropTypes.shape({
    name: PropTypes.string.isRequired,
    ping: PropTypes.shape({
      ip: PropTypes.string,
      time: PropTypes.string,
      localIp: PropTypes.string,
    }),
  }).isRequired,
}

export default createFragmentContainer(
  Server,
  graphql`
    fragment Server_server on Server {
      name,
      ping {
        ip,
        time,
        localIp
      }
    }
  `,
);
