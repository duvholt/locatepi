const fs = require('fs');
const {
  buildClientSchema,
  printSchema,
} = require('graphql/utilities');

const schema = buildClientSchema(require('../../backend/schema.json').data);
fs.writeFileSync(
  `schema.graphql`,
  printSchema(schema),
);
