import { Tabs } from '@mantine/core';
import { BiDetail } from "react-icons/bi";
import { FaCommentAlt } from "react-icons/fa";
import type { Book } from '../../../../types/bookTypes';
import "./styles.scss";

function BookDetailsTabs({book}: {book: Book}) {
  return (
    <Tabs color="gray" defaultValue="description">
      <Tabs.List>
        <Tabs.Tab value="description" leftSection={<BiDetail size={12} />}>
          Description
        </Tabs.Tab>
        <Tabs.Tab value="questions" leftSection={<FaCommentAlt size={12} />}>
          Questions
        </Tabs.Tab>
      </Tabs.List>

      <Tabs.Panel value="description">
        {book.description}
      </Tabs.Panel>

      <Tabs.Panel value="questions">
        No Questions yet
      </Tabs.Panel>

      <Tabs.Panel value="settings">
        Settings tab content
      </Tabs.Panel>
    </Tabs>
  );
}

export default BookDetailsTabs;