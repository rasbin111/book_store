import { useForm } from "@mantine/form";
import "./styles.scss";
import { Button, Flex, Group, Select, TextInput } from "@mantine/core";

const FilterBooks = () => {
  const form = useForm({
    mode: "uncontrolled",
    initialValues: {
      title: "",
      priceMin: 0,
      priceMax: 0,
      author: "",
      language: "",
    },
  });
  return (
    <form className="filter-books-container">
      <TextInput
        label="Title"
        placeholder="Title"
        key={form.key("title")}
        {...form.getInputProps("title")}
      />
      <Select
        label="Author"
        placeholder="Select Author"
        key={form.key("author")}
        {...form.getInputProps("author")}
      />
      <Flex gap="lg">

      <TextInput
        label="Min Price"
        placeholder="Min. Price"
        key={form.key("priceMin")}
        {...form.getInputProps("priceMin")}
        />      
      <TextInput
        label="Max Price"
        placeholder="Max. Price"
        key={form.key("priceMax")}
        {...form.getInputProps("priceMax")}
        />
        </Flex>

      <Select
        label="Language"
        placeholder="Select language"
        key={form.key("language")}
        {...form.getInputProps("language")}
      />
      <Flex gap="lg">
        <Button color="dark"> Filter </Button>
        <Button color="dark"> Reset Filter </Button>
      </Flex>
    </form>
  );
};

export default FilterBooks;
