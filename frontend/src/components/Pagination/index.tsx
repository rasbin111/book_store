import { Pagination } from "@mantine/core";

const CustomPagination = ({
  totalCount,
  pageSize,
  activePage,
  setPage,
}: {
  totalCount: number;
  activePage: number;
  pageSize: number;
  setPage: (val: number) => void;
}) => {
  return (
    <Pagination
      total={Math.ceil(totalCount / pageSize)}
      value={activePage}
      color="#7c2d38"
      onChange={(value) => setPage(value)}
      className="pagination-item"
      mt={48}
    />
  );
};

export default CustomPagination;
